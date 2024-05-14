from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

data = pd.read_csv('data_final_final/data_final_final.csv')
# Eliminar las columnas originales de variables categóricas
data = data.drop(
    columns=['AÑO', 'LOCAL_EQUIPO', 'VISITA_EQUIPO'])

# Seleccionar características y variable objetivo
X_train = data.drop(columns=['RESULTADO'])
y_train = data['RESULTADO']


# Separar en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X_train, y_train, test_size=0.3, random_state=42)

# Crear el clasificador de Random Forest
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)

# Entrenar el modelo
rf_classifier.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = rf_classifier.predict(X_test)

# Calcular la precisión del modelo
accuracy = accuracy_score(y_test, y_pred)
print("Precisión del modelo:", accuracy)
