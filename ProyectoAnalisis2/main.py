from rpy2.robjects import r
import pandas as pd
from rpy2.robjects.packages import importr
from DataFrame_Python import DataFramePython


mongolite = importr('mongolite')
r("library(mongolite)")
conexion = "mng_canal_conn " \
           "<- mongo (collection = 'Canal', db = " \
           "'Proyecto', url = " \
           "'mongodb+srv://Bryan:traceon@cluster0.m8f238i.mongodb.net/?retryWrites=true&w=majority')"
x = r(conexion)
r.assign("mng_canal_conn", x)
obtener_canales = "canales <- mng_canal_conn$find('{}')"
canales_r = r(obtener_canales)
df = pd.DataFrame(canales_r)
orden = ["Suisei Ch", "El Juaniquilador", "Pan Piano",
         "Gawr Gura Ch", "Spreen", "Nanashi Mumei Ch",
         "Vicke Blanka", "MissaSinfonia"]
lista_de_data_frames = DataFramePython().lista_data_pandas(df)
for i in range(len(orden)):
    print(f"Canal: {orden[i]}")
    print(f"\n{lista_de_data_frames[i]}\n")

