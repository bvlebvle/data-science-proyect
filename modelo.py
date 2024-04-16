import pandas as pd
from sklearn.calibration import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler

# Cargando los datos
data_train = pd.read_csv('./TRAIN-<=22.csv', sep=';')
data_test = pd.read_csv('./TEST-23-24.csv', sep=';')


# Limpiar y preparar los datos

# Convertir datos categóricos a numéricos con one-hot encoding
data_train = pd.get_dummies(
    data_train, columns=['EQUIPO_LOCAL', 'EQUIPO_VISITA', 'ARBITRO'])

data_test = pd.get_dummies(
    data_test, columns=['EQUIPO_LOCAL', 'EQUIPO_VISITA', 'ARBITRO'])

label_encoder = LabelEncoder()
data_train['RESULTADO_FINAL'] = label_encoder.fit_transform(
    data_train['RESULTADO_FINAL'])


data_test['RESULTADO_FINAL'] = label_encoder.fit_transform(
    data_test['RESULTADO_FINAL'])

# Escogiendo las columnas relevantes para la predicción
features_train = data_train[['LOCAL_GOL_HT', 'VISITA_GOL_MT', 'LOCAL_TIRO_ARCO', 'VISITA_TIRO_ARCO',
                             'LOCAL_CORNER', 'VISITA_CORNER', 'LOCAL_AMARILLA', 'VISITA_AMARILLA']]
target_train = data_train['RESULTADO_FINAL']

features_test = data_test[['LOCAL_GOL_HT', 'VISITA_GOL_MT', 'LOCAL_TIRO_ARCO', 'VISITA_TIRO_ARCO',
                           'LOCAL_CORNER', 'VISITA_CORNER', 'LOCAL_AMARILLA', 'VISITA_AMARILLA']]
target_test = data_test['RESULTADO_FINAL']

# Escalar las características
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features_train)
features_scaled_test = scaler.fit_transform(features_test)


# Dividir los datos en conjuntos de entrenamiento y prueba
X_train = features_scaled
y_train = target_train

X_test = features_scaled_test
y_test = target_test

# Crear y entrenar el modelo de regresión logística
model = LogisticRegression()
model.fit(X_train, y_train)

# Predecir el conjunto de prueba
y_pred = model.predict(X_test)

# Evaluación del modelo
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred)

print("Accuracy:", accuracy)
print("Confusion Matrix:\n", conf_matrix)
print("Classification Report:\n", report)
