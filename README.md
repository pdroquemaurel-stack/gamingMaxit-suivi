# Suivi Gaming Max it

Debrief quotidien avec Claude Code → mise à jour de `data/suivi.json` → `dashboard.html` → push GitHub.

## Installation (une fois)

1. Dézipper le dossier, par exemple dans `~/Projets/gaming-tracker`.
2. Créer un dépôt **privé** sur GitHub (ex. `gaming-suivi`), sans README.
3. Dans un terminal :
   ```bash
   cd ~/Projets/gaming-tracker
   chmod +x publish.sh
   git init -b main
   git add .
   git commit -m "Initialisation du suivi Gaming"
   git remote add origin https://github.com/<ton-compte>/gaming-suivi.git
   git push -u origin main
   ```
4. Tester le build : `python3 build.py` puis ouvrir `dashboard.html` dans le navigateur.

## Chaque soir

```bash
cd ~/Projets/gaming-tracker
claude
```
puis :
```
/debrief Aujourd'hui : call Swarmio sur le COGS, Youssoufa confirme l'ID unique pour fin novembre...
```
Claude résume → pose ses questions → propose la mise à jour → tu réponds `ok` → il écrit et pousse.

Une nouvelle session par jour : tout le contexte est dans `suivi.json`, pas dans l'historique de conversation.

## Première fois (et avant chaque CODIR)

`/revue` → revue secteur par secteur pour corriger statuts, jalons, dates et blocages. `/revue ESPORT` pour un seul secteur.

## Le mardi

`/hebdo` → brouillon du mail de pré-meeting du weekly.

## Fichiers

| Fichier | Rôle |
|---|---|
| `data/suivi.json` | Source unique : `secteurs` (chantiers + transverses) et `items` (faits, décisions, sujets, actions, blocages) |
| `templates/dashboard_template.html` | Mise en page du dashboard |
| `build.py` | Vérifie le JSON et génère `dashboard.html` |
| `publish.sh` | Build + commit + push |
| `CLAUDE.md` | Règles du PMO pour Claude |
| `.claude/commands/` | Commandes `/debrief`, `/revue` et `/hebdo` |
| `.claude/settings.json` | Autorise le build et le push sans confirmation, interdit le push forcé |
