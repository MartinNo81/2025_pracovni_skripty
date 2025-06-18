# Doplni hodnoty od sloupce id_useku

import pandas as pd
import os
import geopandas as gpd
from simpledbf import Dbf5

names_path = os.path.abspath("C:/Users/martin.novak/testovani/qgis/vrbka/passport/0005_ocislovani/komunikace_-_linie__LineString.dbf")
names_path_new = os.path.abspath("C:/Users/martin.novak/testovani/qgis/vrbka/passport/0005_ocislovani/komunikace_-_linie__LineString_.dbf")

# Načtení DBF souboru (df)
dbf = Dbf5(names_path)
df = dbf.to_dataframe()
############################################################################################
# pridani poradoveho cisla a pismena do id useku
seznam=list()
for x in range(len(df)):
    seznam.append(df.loc[x,"id_kom"])
    number = seznam.count(df.loc[x,"id_kom"])
    df.loc[x, "id_useku"] = number
#############################################################################################
# Převod pandas DataFrame (df) na GeoDataFrame
gdf = gpd.GeoDataFrame(df)

# Uložení zpět do DBF
gdf.to_file(names_path_new, driver='ESRI Shapefile')
