from src.carga import cargar_datos, inspeccionar_datos

def main():
    ruta = "datos/dataset.csv"  # Aquí va la ruta a tu archivo CSV
    datos = cargar_datos(ruta)
    if datos is None:
        print("El programa finalizó sin procesar datos.")
    else:
        print("Carga realizada correctamente.")
        inspeccionar_datos(datos)

if __name__ == "__main__":
    main()