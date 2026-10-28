import pandas as pd

def cargar_datos(ruta='datos/dataset.csv'):
    """Carga el dataset de precipitaciones desde un archivo CSV."""
    df = pd.read_csv(ruta)
    return df

def inspeccionar_datos(df):
    """Realiza la inspección inicial mostrando dimensiones, columnas, tipos y nulos."""
    print("==================================================")
    print("   INSPECCIÓN INICIAL DE DATOS: PRECIPITACIONES")
    print("==================================================")
    print(f"Dimensiones del dataset (filas, columnas): {df.shape}")
    print(f"Columnas detectadas: {list(df.columns)}")
    print("\nTipos de datos asignados:\n", df.dtypes)
    print("\nRecuento de valores nulos:\n", df.isnull().sum())
    print(f"Registros duplicados: {df.duplicated().sum()}")
