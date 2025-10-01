import random


def simulador_ruleta():
    """
    Simula 1000 tiradas de una ruleta  y muestra estadísticas sobre los resultados.
    """
    # Definimos los números de la ruleta
    numeros_rojos = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}

    # Inicializamos los contadores
    pares = 0
    impares = 0
    docena1 = 0  # 1-12
    docena2 = 0  # 13-24
    docena3 = 0  # 25-36
    ceros = 0
    rojos = 0
    negros = 0

    total_tiradas = 1000

    # Realizamos las 1000 tiradas
    for _ in range(total_tiradas):
        numero = random.randint(0, 36)
        # Contabilizamos el cero
        if numero == 0:
            ceros += 1
        else:
            # Contabilizamos pares e impares
            if numero % 2 == 0:
                pares += 1
            else:
                impares += 1

            # Contabilizamos por docena
            if 1 <= numero <= 12:
                docena1 += 1
            elif 13 <= numero <= 24:
                docena2 += 1
            elif 25<= numero <= 36:  # 25 <= numero <= 36
                docena3 += 1

            # Contabilizamos por color
            if numero in numeros_rojos:
                rojos += 1
            else:
                negros += 1

    # Calculamos el porcentaje de ceros
    porcentaje_ceros = (ceros / total_tiradas) * 100

    # Mostramos los resultados
    print("--- Resultados de la Simulación de Ruleta (1000 tiradas) ---")

    print("\n## Cantidad por Paridad")
    print(f"**Pares:** {pares}")
    print(f"**Impares:** {impares}")

    print("\n## Cantidad por Docena")
    print(f"**Primera Docena (1-12):** {docena1}")
    print(f"**Segunda Docena (13-24):** {docena2}")
    print(f"**Tercera Docena (25-36):** {docena3}")

    print("\n## Cantidad por Color")
    print(f"**Rojos:** {rojos}")
    print(f"**Negros:** {negros}")

    print("\n## Estadísticas del Cero")
    print(f"**Cantidad de Ceros:** {ceros}")
    print(f"**Porcentaje de Ceros:** {porcentaje_ceros:.2f}%")
    print("\n---------------------------------------------------------")

if __name__ == '__main__':
    simulador_ruleta()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
