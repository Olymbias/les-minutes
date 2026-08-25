from PIL import Image, ImageDraw

VERT   = (40, 92, 54)     # #285C36
CREME  = (244, 239, 227)  # #F4EFE3
OR     = (217, 186, 95)   # #D9BA5F
ROUGE  = (191, 79, 69)    # #BF4F45


def dessiner(taille, maskable=False):
    """Icône façon affiche : des lignes de procès-verbal, un bloc rouge."""
    S = 1024
    img = Image.new("RGB", (S, S), VERT)
    d = ImageDraw.Draw(img)

    # Zone sûre réduite pour la version maskable (Android rogne les bords)
    m = S * 0.24 if maskable else S * 0.16

    # Lignes du procès-verbal, largeurs variées, bien épaisses
    n = 5
    zone_h = S - 2 * m
    ep = zone_h * 0.10           # épaisseur d'une ligne
    pas = zone_h / n
    largeurs = [1.0, 0.72, 0.88, 0.55, 0.80]
    for i in range(n):
        y = m + i * pas + (pas - ep) / 2
        w = (S - 2 * m) * largeurs[i]
        couleur = OR if i == 0 else CREME
        d.rectangle([m, y, m + w, y + ep], fill=couleur)

    # Le point final : un bloc rouge, en bas à droite
    c = ep * 1.15
    d.rectangle([S - m - c, m + (n - 1) * pas + (pas - ep) / 2 - (c - ep) / 2,
                 S - m, m + (n - 1) * pas + (pas - ep) / 2 + ep + (c - ep) / 2],
                fill=ROUGE)

    return img.resize((taille, taille), Image.LANCZOS)


dessiner(192).save("icone-192.png")
dessiner(512).save("icone-512.png")
dessiner(512, maskable=True).save("icone-512-maskable.png")
print("icônes créées")
