import re
import requests

def procesar_texto(texto):
    """
    Limpia y extrae palabras de un texto.
    Convierte a minúsculas, elimina puntuación y números.
    """
    # Convierte el texto a minúsculas
    texto = texto.lower()
    # Reemplaza caracteres no alfabéticos (excepto espacios) por un espacio
    texto = re.sub(r'[^a-z\s]', '', texto)
    # Divide el texto en palabras
    palabras = texto.split()
    return set(palabras)

# --- Paso 1: Procesar el texto del Quijote ---

# Lee el contenido del archivo 'quijote.txt'
try:
    with open('quijote.txt', 'r', encoding='utf-8') as archivo_quijote:
        texto_quijote = archivo_quijote.read()
except FileNotFoundError:
    print("Error: El archivo 'quijote.txt' no se encontró.")
    exit()

# Obtiene un conjunto de palabras únicas del Quijote
palabras_unicas_quijote = procesar_texto(texto_quijote)
cantidad_palabras_quijote = len(palabras_unicas_quijote)

# --- Paso 2: Procesar el diccionario de inglés ---

# URL del diccionario de inglés
url_diccionario = "https://inventwithpython.com/dictionary.txt"

# Descarga el contenido del diccionario
try:
    respuesta = requests.get(url_diccionario)
    respuesta.raise_for_status()  # Lanza un error si la descarga falla
    texto_diccionario = respuesta.text
except requests.exceptions.RequestException as e:
    print(f"Error al descargar el diccionario: {e}")
    exit()

# Obtiene un conjunto de palabras del diccionario
palabras_diccionario = set(texto_diccionario.lower().split())
cantidad_palabras_diccionario = len(palabras_diccionario)

# --- Paso 3: Comparar y obtener resultados ---

# Palabras del Quijote que no están en el diccionario de inglés
palabras_no_encontradas = palabras_unicas_quijote.difference(palabras_diccionario)
cantidad_no_encontradas = len(palabras_no_encontradas)

# Ordenar la lista de palabras no encontradas
lista_ordenada_no_encontradas = sorted(list(palabras_no_encontradas))

# --- Paso 4: Informar los resultados ---

print("--- Análisis del Vocabulario de 'El Quijote' ---")
print(f"Cantidad de palabras únicas en el libro: {cantidad_palabras_quijote}")
print(f"Cantidad de palabras en el diccionario de inglés: {cantidad_palabras_diccionario}")
print(f"Cantidad de palabras del libro que no existen en el diccionario: {cantidad_no_encontradas}")
print("\n--- Listado de Palabras No Encontradas (primeras 100) ---")
for i, palabra in enumerate(lista_ordenada_no_encontradas[:100]):
    print(f"{i+1}. {palabra}")