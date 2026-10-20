---
description: Revue complète d'un ou de tous les secteurs (initialisation du contenu, ou revue avant CODIR)
---

Revue du ou des secteurs suivants : $ARGUMENTS
(vide = tous, dans l'ordre PLAY, SHOP, ESPORT, PART, PILOT, AUTRE)

Objectif : remettre à plat le contenu du dashboard, secteur par secteur. N'écris rien sur disque avant validation.

Pour chaque secteur, un à la fois :

1. **Présente l'état actuel** tel qu'il est dans `data/suivi.json`, lisible (pas de JSON) :
   statut · objectif · prochaine étape · jalons (fait / date) · actions ouvertes · blocages ouverts (avec date d'ouverture).
2. **Pose tes questions** (6 maximum) pour corriger et compléter, en priorité :
   - statut juste ? objectif et prochaine étape toujours d'actualité ?
   - jalons : la liste est-elle la bonne, lesquels sont franchis, quelles dates cibles ?
   - blocages : toujours ouverts ? date d'origine réelle ? qui doit arbitrer ?
   - actions manquantes, avec responsable (Paul, un collègue ou un partenaire), échéance et colonne ;
   - faits ou décisions récents importants à historiser (avec leur date réelle).
3. **Propose la version corrigée** du secteur (ancien → nouveau), puis demande : « Je valide ce secteur ? (ok / corrections) ».
4. Après « ok », mets à jour `data/suivi.json` pour ce secteur seulement, lance le build (`py build.py` sous Windows, `python3 build.py` sur Mac), puis passe au secteur suivant.

Règles spécifiques à la revue :
- Les faits et décisions passés sont datés à leur date réelle (pas à la date du jour). Si Paul ne connaît pas la date exacte, utiliser le 1er du mois concerné et le préciser dans le texte.
- La date d'ouverture d'un blocage (`date`) doit être sa date d'origine réelle : c'est elle qui calcule l'ancienneté.
- À la fin de la revue : récapitulatif en 5 lignes des changements, puis « Je publie ? ». Après « ok » : `./publish.sh "Revue AAAA-MM-JJ"`.
