/* Service worker — permet à l'app de fonctionner sans connexion.
   Quand tu modifies index.html, change le numéro de VERSION ci-dessous :
   c'est ce qui force le téléphone à recharger la nouvelle version. */
const VERSION = "registre-v1";

const FICHIERS = [
  "./",
  "./index.html",
  "./manifest.json",
  "./icone-192.png",
  "./icone-512.png",
  "./icone-512-maskable.png"
];

// À l'installation : on met les fichiers en cache
self.addEventListener("install", (e) => {
  e.waitUntil(
    caches.open(VERSION)
      .then((cache) => cache.addAll(FICHIERS))
      .then(() => self.skipWaiting())
  );
});

// À l'activation : on supprime les vieux caches
self.addEventListener("activate", (e) => {
  e.waitUntil(
    caches.keys()
      .then((cles) => Promise.all(
        cles.filter((c) => c !== VERSION).map((c) => caches.delete(c))
      ))
      .then(() => self.clients.claim())
  );
});

// À chaque requête : on sert le cache si disponible, sinon le réseau
self.addEventListener("fetch", (e) => {
  if (e.request.method !== "GET") return;
  e.respondWith(
    caches.match(e.request).then((reponse) => reponse || fetch(e.request))
  );
});
