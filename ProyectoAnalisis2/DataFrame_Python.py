import pandas as pd


class DataFramePython:
    def __init__(self):
        self.rango = 4
        self.canales = 8

    def convert(self, df):
        lista_convertida: list = []
        for i in range(self.rango):
            lista_convertida.append(df[i])
        titulos_columnas = ["Suscriptores", "Videos", "Vistas", "Fecha_Hora"]
        dataframe = pd.DataFrame(lista_convertida, titulos_columnas)
        dataframe = pd.DataFrame.transpose(dataframe)
        return dataframe

    def lista_data_pandas(self, df_r):
        lista_pandas: list = []
        for i in range(self.canales):
            nuevo_df = self.convert(df_r[i][1])
            lista_pandas.append(nuevo_df)
        return lista_pandas
