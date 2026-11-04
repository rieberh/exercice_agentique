---
name: pandas-tuto
description: À charger quand l'agent analyste doit répondre avec pandas à une question sur le corpus HYE (les questions Q1 à Q5 de scripts/analyser.py).
---

Seules les fonctions pandas ci-dessous sont autorisées. On travaille sur des colonnes
entières : pas de boucle `for` sur les lignes d'un tableau.

| Je veux… | pandas |
|---|---|
| lire un TSV | `pd.read_csv(chemin, sep="\t")` | oui |
| afficher le tableau, ses 5 premières / 5 dernières lignes | `df`, `df.head()`, `df.tail()` | oui |
| dimensions, colonnes, statistiques | `df.shape`, `df.columns`, `df.describe()` | oui |
| sélectionner une colonne, puis plusieurs | `df["pos"]`, `df[["pos", "lemma"]]` | oui |
| compter les valeurs d'une colonne (top 5 des `pos`) | `serie.value_counts().head(5)` | oui (`value_counts`, `head`) |
| lister les valeurs uniques d'une colonne | `serie.unique()` | oui |
| filtrer des lignes avec un masque booléen | `df[df["pos"] == "V"]`, `&`, `\|` | oui |
| créer une colonne | `df["longueur"] = df["form"].str.len()` | oui |
| longueur d'une chaîne / présence d'un motif | `serie.str.len()`, `serie.str.contains("@")` | oui |

Toute fonction ajoutée ici alors qu'elle ne figurait pas dans le tableau
récapitulatif du notebook devra être signalée dans `RAPPORT.md`.
---

