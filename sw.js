/* Offline support for the YLE vocab pages.

   The page itself decides what to download (設定 → 離線使用) and stores the
   files in the Cache API under "yle-offline-v1". This worker only answers from
   that cache; anything that was never downloaded goes to the network exactly as
   it would without a service worker, so pages that have not been set up for
   offline use (and any other file on the site) behave as before.

   - pages (.html) and data (.json): network first, cached copy when offline,
     so an online visit always gets the newest version
   - pictures and sounds: cached copy first (fast, works offline), refreshed in
     the background when online so updated files arrive on a later play
   - iPhone Safari asks for audio in byte ranges; cached audio is answered with
     a proper 206 partial response, otherwise it would not play offline
*/
const CACHE = "yle-offline-v1";

self.addEventListener("install", () => self.skipWaiting());
self.addEventListener("activate", (event) => event.waitUntil(self.clients.claim()));

function cacheKey(url) {
  const u = new URL(url);
  u.search = "";
  u.hash = "";
  return u.href;
}

async function cachedResponse(request) {
  const cache = await caches.open(CACHE);
  const key = cacheKey(request.url);
  // the Movers page is index.html, but the site address ends in "/"
  return (await cache.match(key)) || (key.endsWith("/") ? cache.match(key + "index.html") : undefined);
}

const refreshed = new Set(); // refresh each file at most once while this worker runs
async function refresh(url) {
  const key = cacheKey(url);
  if (refreshed.has(key)) return;
  refreshed.add(key);
  try {
    const res = await fetch(url, { cache: "no-cache" });
    if (res.ok && res.status === 200) {
      const cache = await caches.open(CACHE);
      await cache.put(cacheKey(url), res);
    }
  } catch (e) { /* offline: keep the cached copy */ }
}

async function rangeResponse(request, cached) {
  const range = request.headers.get("range");
  const blob = await cached.blob();
  const type = cached.headers.get("content-type") || blob.type || "audio/mpeg";
  if (!range) {
    return new Response(blob, { status: 200, headers: { "Content-Type": type, "Content-Length": String(blob.size), "Accept-Ranges": "bytes" } });
  }
  const m = /bytes=(\d*)-(\d*)/.exec(range);
  let start = m && m[1] ? parseInt(m[1], 10) : 0;
  let end = m && m[2] ? parseInt(m[2], 10) : blob.size - 1;
  if (m && !m[1] && m[2]) { start = Math.max(0, blob.size - parseInt(m[2], 10)); end = blob.size - 1; }
  end = Math.min(end, blob.size - 1);
  if (start >= blob.size || start > end) {
    return new Response(null, { status: 416, headers: { "Content-Range": `bytes */${blob.size}` } });
  }
  return new Response(blob.slice(start, end + 1), {
    status: 206,
    headers: {
      "Content-Type": type,
      "Content-Range": `bytes ${start}-${end}/${blob.size}`,
      "Content-Length": String(end - start + 1),
      "Accept-Ranges": "bytes",
    },
  });
}

self.addEventListener("fetch", (event) => {
  const req = event.request;
  if (req.method !== "GET") return;
  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return;
  const path = url.pathname;
  const isDoc = req.mode === "navigate" || /\.(html|json|webmanifest)$/.test(path) || path.endsWith("/");

  if (isDoc) {
    event.respondWith((async () => {
      const cached = await cachedResponse(req);
      if (!cached) return fetch(req); // never downloaded: plain network
      try {
        const res = await fetch(req, { cache: "no-cache" });
        if (res.ok && res.status === 200) {
          const cache = await caches.open(CACHE);
          cache.put(cacheKey(req.url), res.clone());
        }
        return res;
      } catch (e) {
        return cached;
      }
    })());
    return;
  }

  event.respondWith((async () => {
    const cached = await cachedResponse(req);
    if (!cached) return fetch(req);
    event.waitUntil(refresh(req.url));
    if (/\.(mp3|m4a|ogg|wav)$/.test(path)) return rangeResponse(req, cached);
    return cached;
  })());
});
