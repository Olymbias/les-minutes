# Registre de délibérations / The Minutes

Une PWA — une page web installable sur téléphone comme une vraie app.
Français par défaut, bouton **EN** en haut à droite pour basculer.

---

## Installer sur ton Android

Une PWA doit être servie en **https** pour être installable. Il faut donc
mettre les fichiers en ligne quelque part. Le plus simple et gratuit :

### Option A — GitHub Pages (recommandé)

1. Crée un compte sur github.com si tu n'en as pas.
2. Crée un dépôt public, nomme-le par exemple `registre`.
3. Envoie-y tous les fichiers de ce dossier (bouton « Add file » → « Upload files »).
4. Dans le dépôt : **Settings** → **Pages** → Source : `main`, dossier `/ (root)` → Save.
5. Attends une minute. Ton adresse est `https://TONPSEUDO.github.io/registre/`.
6. Ouvre cette adresse dans **Chrome sur ton Android** → menu ⋮ → **Installer l'application**.

L'icône apparaît sur ton écran d'accueil. L'app s'ouvre en plein écran,
sans barre d'adresse, et fonctionne **sans connexion**.

### Option B — Netlify Drop

Va sur `app.netlify.com/drop` et glisse le dossier entier dans la page.
Tu obtiens une adresse https immédiatement, sans compte.

---

## Mettre à jour les fortunes

Les chiffres viennent de Forbes et sont figés volontairement (voir plus bas).
Pour les rafraîchir :

1. Ouvre `index.html` dans un éditeur de texte.
2. Cherche le tableau `SUJETS` (vers le début du `<script>`).
3. Modifie la valeur `usd` et la mention `releve` :

```js
{ id:"bezos", nom:"Jeff Bezos", usd:290e9, naissance:1964, releve:"Forbes 2026" },
```

`290e9` signifie 290 × 10⁹, soit 290 milliards. Pour 305 milliards : `305e9`.

4. **Important** : ouvre `sw.js` et change `registre-v1` en `registre-v2`.
   Sans ça, les téléphones qui ont déjà l'app garderont l'ancienne version en cache.
5. Renvoie les fichiers modifiés sur GitHub / Netlify.

### Ajouter quelqu'un

Une ligne de plus dans `SUJETS`, avec un `id` unique :

```js
{ id:"zuckerberg", nom:"Mark Zuckerberg", usd:222e9, naissance:1984, releve:"Forbes 2026" },
```

---

## Pourquoi des chiffres figés et pas du temps réel ?

Trois raisons, dans l'ordre d'importance :

1. **Forbes et Bloomberg n'ont pas d'API publique gratuite.** Leurs classements
   sont leur produit ; ils ne les ouvrent pas.
2. **Une bonne partie de ces fortunes n'est pas cotée.** SpaceX, par exemple,
   n'est pas en bourse : aucun cours ne permettrait de la suivre.
3. **Ces chiffres sont de toute façon des estimations théoriques.** Il s'agit
   d'actions non vendues, pas d'argent en banque. La fortune de Musk a varié
   de plusieurs centaines de milliards en quelques semaines en 2026.

Afficher une source datée est donc plus honnête qu'un faux temps réel.

---

## Modifier les textes

Toutes les phrases affichées vivent dans l'objet `TEXTES`, avec une entrée
`fr` et une entrée `en`. **Chaque clé doit exister dans les deux langues**,
sinon l'affichage se casse en basculant.

Les repères historiques (« avant l'agriculture », etc.) sont dans le tableau
`ancres` de chaque langue. Ils sont testés du plus ancien au plus récent :
le premier dont le seuil `min` est atteint gagne.

---

## Les fichiers

| Fichier | Rôle |
|---|---|
| `index.html` | Toute l'app : structure, style, calculs, textes |
| `manifest.json` | Nom, couleurs et icônes vus par Android |
| `sw.js` | Service worker : permet le fonctionnement hors ligne |
| `icone-*.png` | Icônes de l'écran d'accueil |
| `faire_icones.py` | Script qui a généré les icônes (optionnel) |

---

## Sources

- Fortunes : Forbes (date de relevé indiquée pour chaque personne).
- Concentration du patrimoine en 1789 : Thomas Piketty, cité par le CADTM.
  À la veille de la Révolution, le décile le plus riche détenait environ 90 %
  du patrimoine national, et le centile le plus riche environ 60 %.
- Aucune donnée saisie ne quitte l'appareil : il n'y a ni serveur, ni suivi,
  ni stockage.
