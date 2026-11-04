---
name: tagset
description: À charger quand l'agent a besoin du tagset officiel de l'arménien classique (HYE) — définitions des étiquettes `pos` — par exemple pour vérifier quelles étiquettes du corpus figurent dans la liste officielle (question Q4).
---

Le tagset HYE se trouve dans `references/HYE_tagset.txt` : une étiquette par ligne,
suivie d'une tabulation puis de sa définition.

Règles :
- Ne pas modifier cette skill (fichier `references/HYE_tagset.txt` compris).
- Pièges à connaître :
  - certains noms d'étiquettes du tagset se terminent par une espace ;
  - une étiquette composée (parties séparées par `+`) est valide si chacune de ses parties figure dans le tagset.
