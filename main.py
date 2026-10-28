from src.carga import cargar_datos, inspeccionar_datos

if __name__ == "__main__":
    print("Iniciando carga de datos...")
    try:
        # Carga el archivo desde la carpeta datos/
        df = cargar_datos('datos/dataset.csv')
        print("Carga realizada correctamente.\n")
        
        # Ejecuta la inspección inicial
        inspeccionar_datos(df)
        
    except FileNotFoundError:
        print("Error: No se encontró el archivo 'datos/dataset.csv'. Asegúrate de colocarlo en la carpeta correcta.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
