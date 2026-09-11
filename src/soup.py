from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

url = "https://example.com"

headers = {"User-Agent": "Python-Lerndemo/1.0"}

try:
    antwort = requests.get(url, headers=headers, timeout=10)
    antwort.raise_for_status()
except requests.RequestException as fehler:
    print(f"Die Webseite konnte nicht geladen werden: {fehler}")
    raise SystemExit(1)

soup = BeautifulSoup(antwort.text, "html.parser")

titel = soup.title.get_text(strip=True) if soup.title else "Kein Titel"
print(f"Titel: {titel}")

print("Überschriften:")
for ueberschrift in soup.find_all(["h1", "h2", "h3"]):
    print("-", ueberschrift.get_text(" ", strip=True))

print("Links:")
for link in soup.find_all("a", href=True):
    text = link.get_text(" ", strip=True) or "Ohne Linktext"
    ziel = urljoin(url, link["href"])
    print(f"- {text}: {ziel}")
