# skript smaže sloupce v dbf, zachová pouze vypsané (21),
# aplikuje se na všechny dbf v adresáři directory(10), háže do (11)
import pandas as pd
import os
import geopandas as gpd
from simpledbf import Dbf5

############################################################################################
# skript se aplikuje na všechny dbf soubory v adresáři "directory, upravene dbf háže do output_directory složky"
directory = r"c:\Users\martin.novak\testovani\qgis\test"
output_directory = r"c:\Users\martin.novak\testovani\qgis\test\upraveno"

for soubor in os.listdir(directory):
    if soubor.endswith(".dbf"):
        cesta = os.path.join(directory,soubor)
        print(f"zpracovávám soubor. {cesta}")

        # Načtení DBF souboru (df)
        dbf = Dbf5(cesta)
        df = dbf.to_dataframe()
        # Odstranění konkrétního sloupce
        df = df[["tridapresn","tridapre_1","urovenumis"]]
        # nastavení výstupních cest
        vystup = os.path.join(output_directory,soubor)
        gdf = gpd.GeoDataFrame(df)
        gdf.to_file(vystup, driver="ESRI Shapefile")
        print(f"soubor upraven: {vystup}")


