from PIL import Image, ImageDraw

PARCHEMIN = (242, 214, 179)
VERT      = (30, 58, 42)
OR        = (202, 163, 90)
ROUGE     = (166, 49, 38)


def dessiner(taille, maskable=False):
    """Icône : un registre ouvert, trait doré, sceau rouge."""
    S = 1024
    img = Image.new("RGB", (S, S), VERT if not maskable else VERT)
    d = ImageDraw.Draw(img)

    # Zone sûre réduite pour la version maskable (Android rogne les bords)
    m = S * 0.26 if maskable else S * 0.15

    # Page de gauche et de droite (le registre ouvert)
    haut, bas = m, S - m
    milieu = S / 2
    ecart = S * 0.012

    d.rectangle([m, haut, milieu - ecart, bas], fill=PARCHEMIN)
    d.rectangle([milieu + ecart, haut, S - m, bas], fill=PARCHEMIN)

    # Reliure centrale
    d.rectangle([milieu - ecart, haut, milieu + ecart, bas], fill=OR)

    # Lignes d'écriture, plus courtes en descendant (comme une liste)
    trait = max(2, int(S * 0.011))
    n = 5
    zone_h = (bas - haut) * 0.62
    depart = haut + (bas - haut) * 0.19
    pas = zone_h / n
    for i in range(n):
        y = depart + i * pas
        for gauche, droite in ((m, milieu - ecart), (milieu + ecart, S - m)):
            marge = (droite - gauche) * 0.14
            fin = droite - marge - (droite - gauche) * 0.10 * (i % 3)
            d.line([gauche + marge, y, fin, y], fill=VERT, width=trait)

    # Sceau de cire, en bas à droite
    r = S * 0.085
    cx, cy = S - m - r * 1.1, bas - r * 1.1
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=ROUGE)
    d.ellipse([cx - r * 0.62, cy - r * 0.62, cx + r * 0.62, cy + r * 0.62],
              outline=OR, width=max(2, int(S * 0.007)))

    return img.resize((taille, taille), Image.LANCZOS)


dessiner(192).save("icone-192.png")
dessiner(512).save("icone-512.png")
dessiner(512, maskable=True).save("icone-512-maskable.png")
print("icônes créées")
