---
description: Debrief quotidien du projet Gaming — résumé, questions, proposition de mise à jour, puis publication après validation
---

Debrief du jour de Paul (peut être vide, dans ce cas demande-lui de raconter sa journée) :

$ARGUMENTS

Déroule strictement ces 4 étapes. N'écris rien sur disque avant l'étape 4.

## Étape 1 — Contexte (silencieux)
Lis `data/suivi.json` : secteurs et jalons, actions non terminées (`a_planifier`, `prevu`) et blocages `ouvert`. Récupère la date du jour avec `date +%F`.

## Étape 2 — Résumé et questions
Présente en une réponse courte :
- **Ce que j'ai compris**, classé par secteur (Play, Shop, E-sport, puis transverses) (faits, décisions, nouveaux sujets).
- **Questions** (5 maximum, uniquement si la réponse change le suivi) :
  - owner ou échéance manquants sur une action ;
  - un élément qui ressemble à un blocage : qui doit débloquer, quel impact ?
  - un blocage ouvert depuis plus de 7 jours dont Paul n'a pas parlé : toujours d'actualité ?
  - une action arrivée à échéance : faite ou non ?
  - un changement de statut (vert/orange/rouge) ou un jalon franchi ?
- **Point d'attention** (1 ou 2 max) : risque, incohérence ou dépendance que Paul n'a pas relevé.

Attends sa réponse. S'il n'y a aucune question utile, passe directement à l'étape 3.

## Étape 3 — Proposition de mise à jour
Présente la version proposée, lisible (pas de JSON) :
1. **Actualité du jour** — 3 à 6 puces, par secteur.
2. **Décisions**
3. **Actions** — texte · responsable · échéance · colonne (Réalisé / Prévu / À planifier).
4. **Blocages** — nouveaux / mis à jour / fermés.
5. **Secteurs** — changements de statut, jalons franchis, prochaine étape (ancien → nouveau).

Termine par : « Je valide et je publie ? (ok / corrections) ». Attends.
Si Paul corrige, intègre et représente uniquement les parties modifiées, puis redemande validation.

## Étape 4 — Écriture et publication (seulement après « ok »)
1. Mets à jour `data/suivi.json` : nouveaux `items` datés du jour (id suivant), fermetures, secteurs et jalons, `meta.maj`.
2. Lance `./publish.sh "Debrief AAAA-MM-JJ"`.
3. Confirme en une ligne : fichier mis à jour, commit poussé — ou l'erreur exacte si le push échoue. Ne jamais forcer un push.
