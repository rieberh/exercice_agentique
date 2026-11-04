from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

train = pd.read_csv(DATA / "HYE_train.tsv", sep="\t")
test_in = pd.read_csv(DATA / "HYE_test_in-domain.tsv", sep="\t")
test_out = pd.read_csv(DATA / "HYE_test_out-of-domain.tsv", sep="\t")

# Q1 : 5 catégories (pos) les plus fréquentes dans le train
vc = train["pos"].value_counts().head(5)
print("Q1: " + ", ".join(f"{p} ({c})" for p, c in vc.items()))

# Q2 : proportion de formes composées ('@' dans pos) et les 5 combinaisons les plus fréquentes
mask = train["pos"].str.contains("@", na=False)
prop = mask.mean()
top5 = train[mask]["pos"].value_counts().head(5)
print(f"Q2: proportion={prop:.4f} ({prop * 100:.2f}%), top5="
      + ", ".join(f"{p} ({c})" for p, c in top5.items()))

# Q3 : pos finissant par @PRO+Dem ; lemma commençant par «զ@»
pos_s = train["pos"].str.strip()
n_dem = int(pos_s.str.contains(r"@PRO\+Dem$", na=False).sum())
n_z = int(train["lemma"].str.contains(r"^զ@", na=False).sum())
print(f"Q3: pos finissant par @PRO+Dem = {n_dem} ; lemma commençant par «զ@» = {n_z}")

# Q4 : étiquettes du train absentes du tagset
# pièges : espaces finales dans les noms du tagset (strip) ; une étiquette composée
# (parties jointes par '@', ex. I+Prep@PRO+Dem) est valide si chaque partie est dans le tagset
tagdf = pd.read_csv(DATA / "HYE_tagset.txt", sep="\t", header=None)
tags = set(tagdf[0].str.strip().unique())
upos = pd.Series(pos_s.unique())
parts = upos.str.split("@").explode()
valid = parts.isin(tags).groupby(level=0).all()
bad_labels = upos[~valid]
bad = pos_s.value_counts()
bad = bad[bad.index.isin(bad_labels)]
print("Q4: " + (", ".join(f"{p} ({c})" for p, c in bad.items())
                if len(bad) else "aucune étiquette du train n'est absente du tagset"))

# Q5 : dictionnaire de la partie 12 du notebook (form -> pos vu dans le train), score = proportion de pos_dico == pos
dico = train[["form", "pos"]].drop_duplicates("form").rename(columns={"pos": "pos_dico"})


def score(test):
    res = test.merge(dico, on="form", how="left")
    return round((res["pos"] == res["pos_dico"]).mean(), 2)


s_in = score(test_in)
s_out = score(test_out)
print(f"Q5: in-domain={s_in}, out-of-domain={s_out}, baisse={round(s_in - s_out, 2)} "
      f"(grec : 0.73 -> 0.51, baisse 0.22) -> la baisse est moins forte qu'en grec")
