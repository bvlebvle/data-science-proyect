import csv
import pandas as pd


def getStatistics(local, visita, año):

    año = año - 1
    local_data = pd.read_csv("./Estadisticas/local_data.csv", delimiter=",")
    visita_data = pd.read_csv("./Estadisticas/visita_data.csv", delimiter=",")

    # fila local
    fila_local = local_data.loc[(local_data['AÑO'] == año) &
                                (local_data['EQUIPO_LOCAL'].str.upper() == local.upper())]

    # fila visita
    fila_visita = visita_data.loc[(visita_data['AÑO'] == año) &
                                  (visita_data['EQUIPO_VISITA'].str.upper() == visita.upper())]

    columnas_a_eliminar = ['AÑO', 'EQUIPO_LOCAL']
    fila_local_modificada = fila_local.drop(columns=columnas_a_eliminar)

    columnas_a_eliminar = ['AÑO', 'EQUIPO_VISITA']
    fila_visita_modificada = fila_visita.drop(columns=columnas_a_eliminar)

    return fila_local_modificada, fila_visita_modificada


match_data = pd.read_csv("./Estadisticas/datos_combinados.csv", delimiter=",")


# CAMBIAR PARA CREAR NUEVO CSV
año = 2004
fila_match = match_data.loc[(match_data['AÑO'] == año)]


headers = ['AÑO', 'LOCAL_EQUIPO', 'LOCAL_VICTORIAS', ' LOCAL_DERROTAS', ' LOCAL_EMPATES', ' LOCAL_GOL', 'LOCAL_GOL_HT  ', 'LOCAL_AMARILLA ', 'LOCAL_ROJA', 'LOCAL_TIRO_ARCO',
           'VISITA_EQUIPO', 'VISITA_VICTORIAS', ' VISITA_DERROTAS', ' VISITA_EMPATES', ' VISITA_GOL', 'VISITA_GOL_HT  ', 'VISITA_AMARILLA ', 'VISITA_ROJA', 'VISITA_TIRO_ARCO']
new_csv = [headers]

for index, row in fila_match.iterrows():
    local = row['EQUIPO_LOCAL']
    visita = row['EQUIPO_VISITA']
    resultado = row['RESULTADO_FINAL']

    fila_local, fila_visita = getStatistics(local, visita, año)

    new_row = [año, local, fila_local['VICTORIAS'].tolist(), fila_local['DERROTAS'].tolist(), fila_local['EMPATES'].tolist(), fila_local['LOCAL_GOL'].tolist(), fila_local['LOCAL_GOL_HT'].tolist(),  fila_local['LOCAL_AMARILLA'].tolist(), fila_local['LOCAL_ROJA'].tolist(), fila_local['LOCAL_TIRO_ARCO'].tolist(),
               visita, fila_visita['VICTORIAS'].tolist(), fila_visita['DERROTAS'].tolist(), fila_visita['EMPATES'].tolist(), fila_visita['VISITA_GOL'].tolist(), fila_visita['VISITA_GOL_HT'].tolist(), fila_visita['VISITA_AMARILLA'].tolist(), fila_visita['VISITA_ROJA'].tolist(), fila_visita['VISITA_TIRO_ARCO'].tolist(), resultado]

    # print(fila_local['VICTORIAS'].values)
    new_csv.append(new_row)

# Ruta del archivo CSV de salida
csv_file_path = str(año) + ".csv"

# Escribir las filas en el archivo CSV
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    for row in new_csv:
        writer.writerow(row)

print("Archivo CSV creado exitosamente en:", csv_file_path)
