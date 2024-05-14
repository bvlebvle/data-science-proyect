import numpy as np
import pandas as pd


data = pd.read_csv("./all_data.csv", delimiter=";")

# SEPARAR LA FECHA EN TRES COLUMNAS: DIA, MES Y AÑO
data['FECHA'] = pd.to_datetime(data['FECHA'], format='%d/%m/%Y')

data['AÑO'] = data['FECHA'].dt.year

data = data.drop(columns=['FECHA'])


# # Separar el resultado en tres columnas
# aggregation_functions = {
#     'RESULTADO_FINAL': [('VICTORIAS', lambda x: (x == 'H').sum()),
#                         ('DERROTAS', lambda x: (x == 'A').sum()),
#                         ('EMPATES', lambda x: (x == 'D').sum())]
# }

# # Agrupar por año y equipo local
# data_local = data.groupby(['AÑO', 'EQUIPO_LOCAL'])

# print(data_local.head(20))
# # Calcular la suma de cada resultado para cada grupo
# summary_stats = data_local.agg({
#     **dict(aggregation_functions),
#     'LOCAL_GOL': 'sum',  # Goles acumulados
#     'LOCAL_GOL_HT': 'sum',  # Goles acumulados en el primer tiempo
#     'LOCAL_AMARILLA': 'sum',  # Tarjetas amarillas acumuladas
#     'LOCAL_ROJA': 'sum',  # Tarjetas rojas acumuladas
#     'LOCAL_TIRO_ARCO': 'sum'  # Tiros al arco acumulados
# }).reset_index()


# print(summary_stats.head(20))

# # pasar el dataframe a un archivo csv
# summary_stats.to_csv('./local_data.csv', index=False)

data_visita = data.groupby(['AÑO', 'EQUIPO_VISITA'])

aggregation_functions = {
    'RESULTADO_FINAL': [('VICTORIAS', lambda x: (x == 'A').sum()),
                        ('DERROTAS', lambda x: (x == 'H').sum()),
                        ('EMPATES', lambda x: (x == 'D').sum())]
}

# Calcular la suma de cada resultado para cada grupo
summary_stats = data_visita.agg({
    **dict(aggregation_functions),
    'LOCAL_GOL': 'sum',  # Goles acumulados
    'LOCAL_GOL_HT': 'sum',  # Goles acumulados en el primer tiempo
    'LOCAL_AMARILLA': 'sum',  # Tarjetas amarillas acumuladas
    'LOCAL_ROJA': 'sum',  # Tarjetas rojas acumuladas
    'LOCAL_TIRO_ARCO': 'sum'  # Tiros al arco acumulados
}).reset_index()

summary_stats.to_csv('./visita_data.csv', index=False)
