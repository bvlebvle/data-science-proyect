import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Cargar los datos
data = pd.read_csv("./Estadisticas/data_estadisticas.csv", delimiter=";")


# Codificar las variables categóricas
encoder = LabelEncoder()
data['EQUIPO_ENCODED'] = encoder.fit_transform(data['EQUIPO'])
data['LOCAL_VISITA_ENCODED'] = encoder.fit_transform(data['LOCAL_VISITA'])

# Eliminar las columnas originales de variables categóricas
data = data.drop(
    columns=['EQUIPO', 'LOCAL_VISITA'])

# Seleccionar características y variable objetivo
X_train = data.drop(columns=['RESULTADO_FINAL_ENCODED'])
y_train = data['RESULTADO_FINAL_ENCODED']


# Separar en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X_train, y_train, test_size=0.2, random_state=42)

# Escalar características (opcional pero recomendado para regresión logística)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print(X_train_scaled)
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


# Realizar validación cruzada
cv_scores = cross_val_score(model, X_train_scaled, y_train, cv=5)

# Imprimir los resultados de la validación cruzada
print()
print("Cross-validation scores:", cv_scores)
print("Mean cross-validation score:", cv_scores.mean())
print()


# Grafica la relación entre los primeros 30 valores de y_test y y_pred
plt.figure(figsize=(10, 6))
plt.plot(range(100), y_test[:100],
         label='Valores Reales', marker='o', color='blue')
plt.plot(range(100), y_pred[:100],
         label='Predicciones', marker='x', color='red')
plt.xlabel("Índice de Datos")
plt.ylabel("Cantidad de Clientes")
plt.title("Valores Reales vs. Predicciones (Primeros 100 Valores)")
plt.legend()
plt.grid(True)
plt.show()
