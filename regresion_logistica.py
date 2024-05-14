import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Cargar los datos
# data_04 = pd.read_csv("./data_final_final/2004.csv", delimiter=",")
# data_05 = pd.read_csv("./data_final_final/2005.csv", delimiter=",")
# data_06 = pd.read_csv("./data_final_final/2006.csv", delimiter=",")
# data_07 = pd.read_csv("./data_final_final/2007.csv", delimiter=",")
# data_08 = pd.read_csv("./data_final_final/2008.csv", delimiter=",")
# data_09 = pd.read_csv("./data_final_final/2009.csv", delimiter=",")
# data_10 = pd.read_csv("./data_final_final/2010.csv", delimiter=",")
# data_11 = pd.read_csv("./data_final_final/2011.csv", delimiter=",")
# data_12 = pd.read_csv("./data_final_final/2012.csv", delimiter=",")
# data_13 = pd.read_csv("./data_final_final/2013.csv", delimiter=",")

# # Concatenar los datos
# data = pd.concat([data_04, data_05, data_06, data_07, data_08,
#                   data_09, data_10, data_11, data_12, data_13], ignore_index=True)

# # Guardar los datos en un archivo csv
# data.to_csv('data_final_final/data_final_final.csv', index=False)

data = pd.read_csv('data_final_final/data_final_final.csv')
# Eliminar las columnas originales de variables categóricas
data = data.drop(
    columns=['LOCAL_EQUIPO', 'VISITA_EQUIPO'])

# Seleccionar características y variable objetivo
X_train = data.drop(columns=['RESULTADO'])
y_train = data['RESULTADO']


# Separar en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X_train, y_train, test_size=0.3, random_state=42)

# Escalar características (opcional pero recomendado para regresión logística)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Inicializar y entrenar el modelo de regresión logística
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# Hacer predicciones en el conjunto de prueba
y_pred = model.predict(X_test_scaled)

# Evaluación del modelo
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred)

print()
print("Accuracy:", accuracy)
print("Confusion Matrix:\n", conf_matrix)
print("Classification Report:\n", report)
print()


print(len(y_test))
print(len(y_pred))


# Grafica la relación entre los primeros valores de y_test y y_pred
n = 50
plt.figure(figsize=(10, 6))
plt.plot(range(n), y_test[:n],
         label='Valores Reales', marker='o', color='blue')
plt.plot(range(n), y_pred[:n],
         label='Predicciones', marker='x', color='red')
plt.xlabel("Índice de Datos")
plt.ylabel("Cantidad de Clientes")
plt.title("Valores Reales vs. Predicciones (Primeros 100 Valores)")
plt.legend()
plt.grid(True)
plt.show()
