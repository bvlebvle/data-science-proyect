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


def datos(año_cambio):
    match_data = pd.read_csv(
        "./Estadisticas/datos_combinados.csv", delimiter=",")

    año = año_cambio
    fila_match = match_data.loc[(match_data['AÑO'] == año)]

    headers = ['AÑO', 'LOCAL_EQUIPO', 'LOCAL_VICTORIAS', ' LOCAL_DERROTAS', ' LOCAL_EMPATES', ' LOCAL_GOL', 'LOCAL_GOL_HT  ', 'LOCAL_AMARILLA ', 'LOCAL_ROJA', 'LOCAL_TIRO_ARCO',
               'VISITA_EQUIPO', 'VISITA_VICTORIAS', ' VISITA_DERROTAS', ' VISITA_EMPATES', ' VISITA_GOL', 'VISITA_GOL_HT  ', 'VISITA_AMARILLA ', 'VISITA_ROJA', 'VISITA_TIRO_ARCO', 'RESULTADO']
    new_csv = [headers]

    for index, row in fila_match.iterrows():
        local = row['EQUIPO_LOCAL']
        visita = row['EQUIPO_VISITA']
        resultado = row['RESULTADO_FINAL']

        fila_local, fila_visita = getStatistics(local, visita, año)

        # Verificar si alguna de las filas está vacía y continuar con la siguiente iteración si es así
        if fila_local.empty or fila_visita.empty:
            continue

        new_row = [año, local] + fila_local.iloc[0].tolist() + \
            [visita] + fila_visita.iloc[0].tolist() + [resultado]
        new_csv.append(new_row)
    # Ruta del archivo CSV de salida
    csv_file_path = "./data_final_final/" + str(año) + ".csv"

    # Escribir las filas en el archivo CSV
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in new_csv:
            writer.writerow(row)

    print("Archivo CSV creado exitosamente en:", csv_file_path)


for i in range(2004, 2023):
    datos(i)
