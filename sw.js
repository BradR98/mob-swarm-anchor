var CACHE_NAME = 'mob-swarm-anchor-v7';
var ASSETS = [
  './', 
  './index.html', 
  './manifest.json', 
  './icon-192.png', 
  './icon-512.png',
  './src/mob-swarm.js',
  './lib/anchor-audio.js',
  './lib/anchor-headless.js',
  './lib/anchor-input.js',
  './lib/anchor-leaderboard.js',
  './lib/anchor-loop.js',
  './lib/anchor-save.js',
  './lib/anchor-ui.js'
];

self.addEventListener('install', function (e) {
  e.waitUntil(caches.open(CACHE_NAME).then(function (c) { return c.addAll(ASSETS); }).then(function () { return self.skipWaiting(); }));
});

self.addEventListener('activate', function (e) {
  e.waitUntil(
    caches.keys().then(function (keys) {
      return Promise.all(keys.filter(function (k) { return k.startsWith('mob-swarm-anchor-') && k !== CACHE_NAME; }).map(function (k) { return caches.delete(k); }));
    }).then(function () { return self.clients.claim(); })
  );
});

self.addEventListener('fetch', function (e) {
  if (e.request.method !== 'GET') return;
  e.respondWith(
    fetch(e.request, { cache: 'no-cache' }).then(function (res) {
      if (res && res.ok && new URL(e.request.url).origin === location.origin) {
        var copy = res.clone(); caches.open(CACHE_NAME).then(function (c) { c.put(e.request, copy); });
      }
      return res;
    }).catch(function () {
      return caches.match(e.request).then(function (hit) { return hit || caches.match('./index.html'); });
    })
  );
});
self.addEventListener('message', function (e) { if (e.data === 'SKIP_WAITING') self.skipWaiting(); });
