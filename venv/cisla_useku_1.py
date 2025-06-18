# Doplni hodnoty do sloupce "id_kom" v dbf.
# Sloupce se musi jmenovat trida_kom a id_kom.

import pandas as pd
import os
import geopandas as gpd
from simpledbf import Dbf5
import os
import pandas as pd
import geopandas as gpd
from simpledbf import Dbf5
names_path = os.path.abspath("C:/Users/martin.novak/testovani/qgis/vrbka/passport/0005_ocislovani/k_ocislovani.dbf")
#nefunguje vzstup na sitovou cestu, patrne problem s pravy, proto zatim vystup lokalne viz radek 99
names_path_new = os.path.abspath("C:/Users/martin.novak/testovani/qgis/vrbka/passport/0005_ocislovani/k_ocislovani__.dbf")

# Načtení DBF souboru (df)
dbf = Dbf5(names_path)
df = dbf.to_dataframe()
############################################################################################
# pridani poradoveho cisla a pismena do id kom
seznam = list()
sd = 1
opakovat = True
while opakovat:
    for x in range(len(df)):
        if df.loc[x, "id_kom"] == "{0}{1}".format(sd,"a"):
            sd+=1
        else:
            opakovat = False
for x in range(len(df)):
    if df.loc[x, "trida_kom"] == 6 and pd.isnull(df.loc[x, "id_kom"]) :
        seznam.append("a")
        number = seznam.count("a") + sd -1
        df.loc[x, "id_kom"] = ("{0}{1}".format(number, "a"))

seznam = list()
sd = 1
opakovat = True
while opakovat:
    for x in range(len(df)):
        if df.loc[x, "id_kom"] == "{0}{1}".format(sd,"b"):
            sd+=1
        else:
            opakovat = False
for x in range(len(df)):
    if df.loc[x, "trida_kom"] == 7 and pd.isnull(df.loc[x, "id_kom"]) :
        seznam.append("b")
        number = seznam.count("b") + sd -1
        df.loc[x, "id_kom"] = ("{0}{1}".format(number, "b"))

seznam = list()
sd = 1
opakovat = True
while opakovat:
    for x in range(len(df)):
        if df.loc[x, "id_kom"] == "{0}{1}".format(sd,"c"):
            sd+=1
        else:
            opakovat = False
for x in range(len(df)):
    if df.loc[x, "trida_kom"] == 8 and pd.isnull(df.loc[x, "id_kom"]) :
        seznam.append("c")
        number = seznam.count("c") + sd -1
        df.loc[x, "id_kom"] = ("{0}{1}".format(number, "c"))

seznam = list()
sd = 1
opakovat = True
while opakovat:
    for x in range(len(df)):
        if df.loc[x, "id_kom"] == "{0}{1}".format(sd,"d"):
            sd+=1
        else:
            opakovat = False
for x in range(len(df)):
    if df.loc[x, "trida_kom"] == 9 and pd.isnull(df.loc[x, "id_kom"]) :
        seznam.append("d")
        number = seznam.count("d") + sd -1
        df.loc[x, "id_kom"] = ("{0}{1}".format(number, "d"))

seznam = list()
sd = 1
opakovat = True
while opakovat:
    for x in range(len(df)):
        if df.loc[x, "id_kom"] == "{0}{1}".format(sd,"e"):
            sd+=1
        else:
            opakovat = False
for x in range(len(df)):
    if df.loc[x, "trida_kom"] == 10 and pd.isnull(df.loc[x, "id_kom"]) :
        seznam.append("e")
        number = seznam.count("e") + sd -1
        df.loc[x, "id_kom"] = ("{0}{1}".format(number, "e"))

seznam = list()
sd = 1
opakovat = True
while opakovat:
    for x in range(len(df)):
        if df.loc[x, "id_kom"] == "{0}{1}".format("S3_",sd):
            sd+=1
        else:
            opakovat = False
for x in range(len(df)):
    if df.loc[x, "trida_kom"] == 5 and pd.isnull(df.loc[x, "id_kom"]) :
        seznam.append("S3")
        number = seznam.count("S3") + sd -1
        df.loc[x, "id_kom"] = ("{0}{1}".format("S3_",number))
#############################################################################################
# Převod pandas DataFrame (df) na GeoDataFrame
gdf = gpd.GeoDataFrame(df)

# Uložení zpět do DBF
gdf.to_file(names_path_new, driver='ESRI Shapefile')
