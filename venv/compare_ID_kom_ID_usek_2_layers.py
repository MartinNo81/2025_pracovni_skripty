# vstupem je passport_axes a passport shapes
# hledá id_kom a id_useku v obou sadách vzájemne
# zkontroluje jestli hodnota delka,plocha pro shodne id_kom a id_useku je shodna

import pandas as pd
import os
import geopandas as gpd
from simpledbf import Dbf5

input1 = os.path.abspath("C:/Users/martin.novak/testovani/qgis/__qqq/osa.dbf")
input2 = os.path.abspath("C:/Users/martin.novak/testovani/qgis/__qqq/obvod.dbf")
output = os.path.abspath("C:/Users/martin.novak/testovani/qgis/__qqq/output.txt")

# Načtení DBF souboru (df)
dbf1 = Dbf5(input1)
dbf2 = Dbf5(input2)
df1 = dbf1.to_dataframe()
df2 = dbf2.to_dataframe()
############################################################################################
df1['kontrola'] = "" # vytvoření sloupce spojujiciho id_kom a id_useku
df1['kontrola'] = df1['id_kom'].astype(str) + (" ") + df1['id_useku'].astype(str) # naplneni sloupce daty = str(df.loc['id_kom'])+str(df.loc['id_useku'])# naplneni sloupce daty
df2['kontrola'] = "" # vytvoření sloupce spojeujuciho id_kom a id_useku
df2['kontrola'] = df2['id_kom'].astype(str) +(" ") +df2['id_useku'].astype(str) # naplneni sloupce daty

seznam_1 = list()
seznam_2 = list()
for x in range(len(df1)):
    if pd.notna(df1.loc[x,"plocha"]):
        seznam_1.append(df1.loc[x,'kontrola'])
for y in range(len(df2)):
    seznam_2.append(df2.loc[y,'kontrola'])

with open(output,"w",encoding="utf-8") as soubor:
    soubor.write("kontrola, zda id_kom, id_useku v axis je i v shapes\n")
for i in seznam_1:
   if i not in seznam_2:
        with open(output,"a",encoding="utf-8") as soubor:
            soubor.write(f"{i}\n")

with open(output,"a",encoding="utf-8") as soubor:
    soubor.write("kontrola, zda id_kom, id_useku v shapes je i v axes\n")
for i in seznam_2:
    if i not in seznam_1:
        with open(output, "a", encoding="utf-8") as soubor:
            soubor.write(f"{i}\n")


with open(output,"a",encoding="utf-8") as soubor:
    soubor.write("kontrola, zda hodnoty ve sloupcich delka, plocha jsou totozne v axis i shapes\n")
for x in range(len(df2)):
    y = df2.loc[x,'kontrola']
    delka_df2 = df2.loc[df2['kontrola'] == y, 'delka']
    delka_df1 = df1.loc[df1['kontrola'] == y, 'delka']

    # Ověříme, zda obě série nejsou prázdné a porovnáme jejich hodnoty
    if not delka_df2.empty and not delka_df1.empty:
        if delka_df2.values[0] != delka_df1.values[0]:  # Porovnáme první nalezenou hodnotu
            with open(output, "a", encoding="utf-8") as soubor:
                soubor.write(f"{y}\n")
    else:
        print(f"Hodnota pro kontrolu '{y}' nebyla nalezena v jednom z DataFrame.")

for x in range(len(df2)):
    y = df2.loc[x,'kontrola']
    delka_df2 = df2.loc[df2['kontrola'] == y, 'plocha']
    delka_df1 = df1.loc[df1['kontrola'] == y, 'plocha']

    # Ověříme, zda obě série nejsou prázdné a porovnáme jejich hodnoty
    if not delka_df2.empty and not delka_df1.empty:
        if delka_df2.values[0] != delka_df1.values[0]:  # Porovnáme první nalezenou hodnotu
            with open(output, "a", encoding="utf-8") as soubor:
                soubor.write(f"{y}\n")
    else:
        print(f"Hodnota pro kontrolu '{y}' nebyla nalezena v jednom z DataFrame.")













