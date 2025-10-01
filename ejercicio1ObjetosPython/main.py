# main.py
import csv
from persona import Persona # Importamos la clase que creamos

def procesar_personas(ruta_archivo):
    """
    Lee un archivo CSV, crea instancias de Persona y las almacena en un diccionario.
    Luego, muestra varios informes basados en los datos cargados.
    """
    personas_dic = {}

    try:
        with open(ruta_archivo, mode='r', encoding='utf-8') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)

            # Iteramos sobre cada línea del archivo
            for linea in lector_csv:
                documento, nombre, apellido, edad = linea
                # Creamos una instancia de Persona
                nueva_persona = Persona(documento, nombre, apellido, edad)
                # La guardamos en el diccionario, usando el documento como clave
                personas_dic[nueva_persona.documento] = nueva_persona

    except FileNotFoundError:
        print(f"Error: El archivo '{ruta_archivo}' no fue encontrado.")
        return # Salimos de la función si no hay archivo

    # --- Generación de Informes ---
    print("--- Informes sobre las Personas Cargadas ---")

    # 1. Cantidad de personas cargadas
    cantidad_personas = len(personas_dic)
    print(f"✅ Cantidad total de personas cargadas: {cantidad_personas}")

    # 2. Cantidad de personas mayores de edad
    mayores_de_edad = sum(1 for p in personas_dic.values() if p.edad >= 18)
    print(f"✅ Cantidad de personas mayores de edad: {mayores_de_edad}")

    # 3. Listado de personas cuyo apellido empieza en vocal
    print("\n✅ Personas cuyo apellido empieza con vocal:")
    vocales = "AEIOU"
    encontrado = False
    for p in personas_dic.values():
        if p.apellido.strip().upper().startswith(tuple(vocales)):
            print(f"  - {p.nombre} {p.apellido}")
            encontrado = True
    if not encontrado:
        print("  - Ninguna persona encontrada.")


    # 4. Cantidad de personas por cada apellido
    print("\n✅ Cantidad de personas por apellido:")
    conteo_apellidos = {}
    for p in personas_dic.values():
        apellido = p.apellido
        # .get(apellido, 0) devuelve el valor actual o 0 si no existe
        conteo_apellidos[apellido] = conteo_apellidos.get(apellido, 0) + 1

    for apellido, cantidad in conteo_apellidos.items():
        print(f"  - {apellido}: {cantidad} persona(s)")


if __name__ == '__main__':
    nombre_archivo = "personas.csv"
    procesar_personas(nombre_archivo)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
