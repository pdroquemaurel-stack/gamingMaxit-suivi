"""Génère dashboard.html à partir de data/suivi.json.

Usage : python3 build.py
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent
DATA_FILE = ROOT / "data" / "suivi.json"
TEMPLATE_FILE = ROOT / "templates" / "dashboard_template.html"
OUTPUT_FILE = ROOT / "dashboard.html"
PLACEHOLDER = "/*__DATA__*/null"

TYPES = {"fait", "decision", "sujet", "action", "blocage"}
STATUTS_SECTEUR = {"vert", "orange", "rouge", "gris"}


def check(data):
    """Contrôles simples pour éviter de publier un fichier incohérent."""
    errors = []
    secteurs = {s["id"] for s in data["secteurs"]}

    for s in data["secteurs"]:
        if s["statut"] not in STATUTS_SECTEUR:
            errors.append(f"Secteur {s['id']} : statut inconnu '{s['statut']}'")

    ids = set()
    for item in data["items"]:
        if item["id"] in ids:
            errors.append(f"Item {item['id']} : id en double")
        ids.add(item["id"])
        if item["secteur"] not in secteurs:
            errors.append(f"Item {item['id']} : secteur inconnu '{item['secteur']}'")
        if item["type"] not in TYPES:
            errors.append(f"Item {item['id']} : type inconnu '{item['type']}'")
        if item["type"] == "action":
            if item.get("statut") not in ("a_planifier", "prevu", "fait"):
                errors.append(f"Item {item['id']} : statut d'action doit être 'a_planifier', 'prevu' ou 'fait'")
            if not item.get("owner"):
                errors.append(f"Item {item['id']} : une action doit avoir un responsable")
        if item["type"] == "blocage" and item.get("statut") not in ("ouvert", "ferme"):
            errors.append(f"Item {item['id']} : statut de blocage doit être 'ouvert' ou 'ferme'")

    seen = set()
    for item in data["items"]:
        key = (item["secteur"], item["type"], item["texte"].strip().lower())
        if key in seen:
            errors.append(f"Item {item['id']} : doublon (même secteur, type et texte)")
        seen.add(key)

    return errors


def main():
    data = json.loads(DATA_FILE.read_text(encoding="utf-8"))

    errors = check(data)
    if errors:
        print("Build annulé :")
        for e in errors:
            print(" -", e)
        sys.exit(1)

    template = TEMPLATE_FILE.read_text(encoding="utf-8")
    if PLACEHOLDER not in template:
        print("Build annulé : marqueur de données absent du gabarit")
        sys.exit(1)

    # "</" est échappé pour qu'un texte ne puisse pas fermer la balise <script>
    data_js = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    OUTPUT_FILE.write_text(template.replace(PLACEHOLDER, data_js), encoding="utf-8")
    print(f"dashboard.html généré ({len(data['secteurs'])} secteurs, {len(data['items'])} items)")


if __name__ == "__main__":
    main()
