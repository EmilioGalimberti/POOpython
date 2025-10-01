import random

def simulador_ruleta_optimizado():
    """
    Simula 1000 tiradas de ruleta con una lógica de conteo más compacta.
    """
    # El set para los números rojos ya es la forma más eficiente para búsquedas.
    numeros_rojos = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}

    # Usamos un diccionario para agrupar todos los contadores
    contadores = {
        'pares': 0, 'impares': 0,
        'rojos': 0, 'negros': 0,
        'ceros': 0
    }
    # Usamos una lista para las docenas para acceder por índice
    docenas = [0, 0, 0] # [1ra docena, 2da docena, 3ra docena]

    total_tiradas = 1000

    for _ in range(total_tiradas):
        numero = random.randint(0, 36)

        if numero == 0:
            contadores['ceros'] += 1
        else:
            # Contabilizamos paridad usando una expresión condicional
            contadores['pares'] += (numero % 2 == 0)
            contadores['impares'] += (numero % 2 != 0)

            # Contabilizamos color
            if numero in numeros_rojos:
                contadores['rojos'] += 1
            else:
                contadores['negros'] += 1

            # ⭐ Optimización: Cálculo directo del índice de la docena
            indice_docena = (numero - 1) // 12
            docenas[indice_docena] += 1

    # --- Presentación de resultados ---
    porcentaje_ceros = (contadores['ceros'] / total_tiradas) * 100

    print("--- Resultados de la Simulación de Ruleta (1000 tiradas) ---")

    print("\n## Cantidad por Paridad")
    print(f"**Pares:** {contadores['pares']}")
    print(f"**Impares:** {contadores['impares']}")

    print("\n## Cantidad por Docena")
    print(f"**Primera Docena (1-12):** {docenas[0]}")
    print(f"**Segunda Docena (13-24):** {docenas[1]}")
    print(f"**Tercera Docena (25-36):** {docenas[2]}")

    print("\n## Cantidad por Color")
    print(f"**Rojos:** {contadores['rojos']}")
    print(f"**Negros:** {contadores['negros']}")

    print("\n## Estadísticas del Cero")
    print(f"**Cantidad de Ceros:** {contadores['ceros']}")
    print(f"**Porcentaje de Ceros:** {porcentaje_ceros:.2f}%")
    print("\n---------------------------------------------------------")


if __name__ == '__main__':
    simulador_ruleta_optimizado()