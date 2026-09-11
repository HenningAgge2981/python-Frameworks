from pathlib import Path

import cv2

datei = Path("foto.jpg")

if not datei.exists():
    raise FileNotFoundError("Bitte ein Bild mit dem Namen foto.jpg ablegen.")

bild = cv2.imread(str(datei))

if bild is None:
    raise ValueError("Das Bild konnte nicht gelesen werden.")

# Größe für die Demo reduzieren
bild = cv2.resize(bild, (800, 500))

# Graustufen und leichte Glättung
grau = cv2.cvtColor(bild, cv2.COLOR_BGR2GRAY)
weich = cv2.GaussianBlur(grau, (5, 5), 0)

# Kanten erkennen
kanten = cv2.Canny(weich, 60, 150)

# Anzahl der äußeren Konturen bestimmen
konturen, _ = cv2.findContours(kanten, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

ergebnis = bild.copy()
cv2.drawContours(ergebnis, konturen, -1, (0, 255, 0), 2)

print(f"Erkannte Konturen: {len(konturen)}")

cv2.imwrite("kanten.jpg", kanten)
cv2.imwrite("konturen.jpg", ergebnis)

cv2.imshow("Erkannte Konturen", ergebnis)
cv2.waitKey(0)
cv2.destroyAllWindows()
