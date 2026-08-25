# Les Minutes / The Minutes

Une PWA — une page web installable sur téléphone comme une vraie app.
Français par défaut, bouton **EN** en haut à droite pour basculer.

---

## Installer sur ton Android

Une PWA doit être servie en **https** pour être installable. Le plus simple :

### Option A — GitHub Pages

1. Dans ton dépôt GitHub, remplace les anciens fichiers par ceux-ci
   (« Add file » → « Upload files » : les fichiers du même nom sont écrasés).
2. Vérifie que `index.html` est bien **à la racine** du dépôt, pas dans un sous-dossier.
3. Settings → Pages → Source : branche `main`, dossier `/ (root)` → Save.
4. L'adresse apparaît dans un encadré en haut de Settings → Pages.
5. Ouvre-la dans **Chrome sur ton Android** → menu ⋮ → **Installer l'application**.

### Option B — Netlify Drop

Va sur `app.netlify.com/drop` et glisse le contenu du dossier dans la page.

---

## Mettre à jour les fortunes

1. Ouvre `index.html`, cherche le tableau `SUJETS` (début du `<script>`).
2. Modifie la valeur `usd` et la mention `releve` :

```js
{ id:"bezos", famille:"Bezos", nom:"Jeff Bezos", usd:290e9, releve:"Forbes 2026" },
```

`290e9` = 290 milliards. Pour 305 milliards : `305e9`.

3. **Important** : dans `sw.js`, change `minutes-v1` en `minutes-v2`.
   Sans ça, les téléphones qui ont déjà l'app garderont l'ancienne version en cache.
4. Renvoie les fichiers modifiés en ligne.

Le compteur « Pendant ce temps » se met à jour tout seul : il est calculé
directement à partir de la fortune affichée (étalée sur un an), sans autre donnée.

### Ajouter quelqu'un

Une ligne de plus dans `SUJETS`, avec un `id` unique :

```js
{ id:"zuckerberg", famille:"Zuckerberg", nom:"Mark Zuckerberg", usd:222e9, releve:"Forbes 2026" },
```

`famille` est ce qui s'affiche dans le menu ; `nom` apparaît dans
« Chiffres & sources » et dans le texte copié.

---

## Pourquoi des chiffres figés et pas du temps réel ?

1. **Forbes et Bloomberg n'ont pas d'API publique gratuite.**
2. **Une bonne partie de ces fortunes n'est pas cotée en bourse** (SpaceX, par exemple).
3. **Ces montants sont des estimations théoriques** : des actions non vendues,
   pas de l'argent en banque. Ils varient de dizaines de milliards en quelques semaines.

Afficher une source datée est plus honnête qu'un faux temps réel.

---

## Modifier les textes

Toutes les phrases vivent dans l'objet `TEXTES` du `<script>`, avec une entrée
`fr` et une entrée `en`. **Chaque clé doit exister dans les deux langues**,
sinon l'affichage se casse en basculant.

Les repères historiques sont dans le tableau `ancres` de chaque langue,
testés du plus ancien au plus récent : le premier seuil `min` atteint gagne.

---

## Les fichiers

| Fichier | Rôle |
|---|---|
| `index.html` | Toute l'app : structure, style, calculs, textes |
| `manifest.json` | Nom, couleurs et icônes vus par Android |
| `sw.js` | Service worker : fonctionnement hors ligne |
| `icone-*.png` | Icônes de l'écran d'accueil |
| `faire_icones.py` | Script qui a généré les icônes (optionnel) |

---

## Sources

- Fortunes : Forbes (date de relevé indiquée pour chaque personne
  dans le volet « Chiffres & sources » de l'app et dans le code).
- Aucune donnée saisie ne quitte l'appareil : ni serveur, ni suivi, ni stockage.
