self.addEventListener('install', event => {
    event.waitUntil(
        caches.open('chat-app-v1').then(cache => {
            return cache.addAll([
                '/',
                '/static/styles.css',
                '/static/app.js',
                '/static/manifest.json',
                '/static/icon.png',
                '/static/icon-512.png'
            ]);
        })
    );
});

self.addEventListener('fetch', event => {
    event.respondWith(
        caches.match(event.request).then(response => {
            return response || fetch(event.request);
        })
    );
});