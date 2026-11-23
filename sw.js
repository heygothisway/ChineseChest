const CACHE_NAME = 'chinese-chest-v1';
const TAILWIND_URL = 'https://cdn.tailwindcss.com/3.4.17';
const APP_FILES = [
  './',
  './index.html',
  './manifest.webmanifest',
  './icons/icon-192.png',
  './icons/icon-512.png',
  './icons/maskable-192.png',
  './icons/maskable-512.png'
];

self.addEventListener('install', event => {
  event.waitUntil((async () => {
    const cache = await caches.open(CACHE_NAME);
    await cache.addAll(APP_FILES);
    const tailwindRequest = new Request(TAILWIND_URL, { mode: 'no-cors' });
    await cache.put(tailwindRequest, await fetch(tailwindRequest));
    await self.skipWaiting();
  })());
});

self.addEventListener('activate', event => {
  event.waitUntil((async () => {
    const names = await caches.keys();
    await Promise.all(names.filter(name => (name.startsWith('chinese-chest-') || name === 'chinese-chess-v1') && name !== CACHE_NAME)
      .map(name => caches.delete(name)));
    await self.clients.claim();
  })());
});

self.addEventListener('fetch', event => {
  if (event.request.method !== 'GET') return;

  if (event.request.mode === 'navigate') {
    event.respondWith(fetch(event.request).catch(() => caches.match('./index.html')));
  } else if (event.request.url === TAILWIND_URL ||
             new URL(event.request.url).origin === self.location.origin) {
    event.respondWith(caches.match(event.request).then(response => response || fetch(event.request)));
  }
});
