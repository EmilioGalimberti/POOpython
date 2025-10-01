# main.py
import csv
from empleado import Obrero, Administrativo, Vendedor


def cargar_empleados(ruta_archivo):
    """
    Lee el archivo CSV y devuelve un diccionario de empleados,
    usando el legajo como clave.
    """
    empleados_dic = {}
    try:
        with open(ruta_archivo, mode='r', encoding='utf-8') as archivo_csv:
            # Usamos ; como delimitador
            lector_csv = csv.reader(archivo_csv, delimiter=';')

            for linea in lector_csv:
                tipo, legajo, nombre, apellido, sueldo_basico, dato_extra = linea

                nuevo_empleado = None
                if tipo == '1':  # Obrero
                    nuevo_empleado = Obrero(legajo, nombre, apellido, sueldo_basico, dato_extra)
                elif tipo == '2':  # Administrativo
                    nuevo_empleado = Administrativo(legajo, nombre, apellido, sueldo_basico, dato_extra)
                elif tipo == '3':  # Vendedor
                    nuevo_empleado = Vendedor(legajo, nombre, apellido, sueldo_basico, dato_extra)

                if nuevo_empleado:
                    empleados_dic[nuevo_empleado.legajo] = nuevo_empleado

    except FileNotFoundError:
        print(f"Error: El archivo '{ruta_archivo}' no se encontró.")
        return None

    return empleados_dic


def main():
    """Función principal del programa."""
    empleados = cargar_empleados('empleados.csv')

    if not empleados:
        return  # Si no se cargaron empleados, termina el programa

    # 1. Calcular el total a pagar de sueldos
    total_sueldos = sum(emp.calcular_sueldo() for emp in empleados.values())
    print(f"💰 Total a pagar en sueldos: ${total_sueldos:,.2f}\n")

    # 2. Contar los empleados por tipo
    conteo_obreros = sum(1 for emp in empleados.values() if isinstance(emp, Obrero))
    conteo_administrativos = sum(1 for emp in empleados.values() if isinstance(emp, Administrativo))
    conteo_vendedores = sum(1 for emp in empleados.values() if isinstance(emp, Vendedor))

    print("📊 Cantidad de empleados por tipo:")
    print(f"  - Obreros: {conteo_obreros}")
    print(f"  - Administrativos: {conteo_administrativos}")
    print(f"  - Vendedores: {conteo_vendedores}\n")

    # 3. Buscar un empleado por legajo
    print("🔍 Búsqueda de empleado por legajo")
    while True:
        try:
            legajo_buscado = input("Ingrese el legajo a buscar (o 'salir' para terminar): ")
            if legajo_buscado.lower() == 'salir':
                break

            legajo_num = int(legajo_buscado)
            empleado_encontrado = empleados.get(legajo_num)

            if empleado_encontrado:
                sueldo = empleado_encontrado.calcular_sueldo()
                print(f"  -> Empleado: {empleado_encontrado.nombre_completo}")
                print(f"  -> Sueldo a pagar: ${sueldo:,.2f}\n")
            else:
                print("  -> No se encontró ningún empleado con ese legajo.\n")
        except ValueError:
            print("  -> Por favor, ingrese un número de legajo válido.\n")


# --- Ejecución del Programa ---
if __name__ == "__main__":
    main()