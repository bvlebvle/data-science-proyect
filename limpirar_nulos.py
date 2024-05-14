import pandas as pd

# Cargar el archivo original
df = pd.read_csv('2004.csv')

# Reemplazar cadenas vacías y espacios con NaN
df.replace({"": pd.NA, " ": pd.NA}, inplace=True)

# Revisar cada columna y reemplazar cadenas que indican ausencia de datos con NaN
for column in df.columns:
    df[column] = df[column].apply(lambda x: pd.NA if isinstance(x, str) and (x.strip() == '-' or not x.strip()) else x)

# Convertir todas las columnas a tipos numéricos si es posible, reteniendo NaNs
df = df.apply(pd.to_numeric, errors='ignore')
df_cleaned = df.dropna()
# Guardar el DataFrame limpio
df_cleaned.to_csv('data_cleaned.csv', index=False)
