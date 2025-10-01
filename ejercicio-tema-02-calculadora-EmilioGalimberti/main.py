# Paso 1: Definir las funciones para cada operación

def sumar(a, b):
    """Esta función toma dos números y devuelve su suma."""
    return a + b


def restar(a, b):
    """Esta función toma dos números y devuelve su diferencia."""
    return a - b


def multiplicar(a, b):
    """Esta función toma dos números y devuelve su producto."""
    return a * b


def dividir(a, b):
    """
    Esta función toma dos números y devuelve su cociente.
    Incluye un control para evitar la división por cero.
    """
    if b == 0:
        return "Error: No se puede dividir por cero."
    return a / b


# Paso 2: Crear el diccionario de operaciones
# Las claves son las opciones del menú y los valores son las funciones que definimos.
operaciones = {
    '1': sumar,
    '2': restar,
    '3': multiplicar,
    '4': dividir
}


# Paso 3: Función principal que ejecuta la calculadora

def calculadora():
    """Función principal para ejecutar la calculadora y el menú."""
    while True:
        print("\n--- Calculadora Básica ---")
        print("Selecciona una operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

        opcion = input("Ingresa tu opción (1/2/3/4/5): ")

        if opcion == '5':
            print("¡Hasta luego! Gracias por usar la calculadora. 👋")
            break

        # Verificamos si la opción elegida está en nuestro diccionario
        if opcion in operaciones:
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
            except ValueError:
                print("Error: Por favor, ingresa solo números.")
                continue  # Vuelve al inicio del bucle

            # Obtenemos la función del diccionario usando la opción como clave
            funcion_a_ejecutar = operaciones[opcion]

            # Ejecutamos la función con los números del usuario
            resultado = funcion_a_ejecutar(num1, num2)

            print("------------------------------")
            print(f"El resultado es: {resultado}")
            print("------------------------------")

        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 5.")


# Iniciar la calculadora
calculadora()