# Es para intentar aplicar lo mas posible los diccionarios

import math

# --- CONFIGURACIÓN CENTRAL DE LA APLICACIÓN ---
# Todo el comportamiento y texto de la calculadora se define aquí.

configuracion = {
    'operaciones': {
        '1': {'funcion': lambda a, b: a + b, 'num_args': 2, 'texto': 'Suma'},
        '2': {'funcion': lambda a, b: a - b, 'num_args': 2, 'texto': 'Resta'},
        '3': {'funcion': lambda a, b: a * b, 'num_args': 2, 'texto': 'Multiplicación'},
        '4': {'funcion': lambda a, b: "Error: División por cero" if b == 0 else a / b, 'num_args': 2,
              'texto': 'División'},
        '5': {'funcion': lambda a, b: a ** b, 'num_args': 2, 'texto': 'Potencia'},
        '6': {'funcion': lambda a: "Error: Raíz de negativo" if a < 0 else math.sqrt(a), 'num_args': 1,
              'texto': 'Raíz Cuadrada'}
    },
    'textos': {
        'titulo': "\n--- Calculadora Configurable ---",
        'menu_principal': {
            # Las claves aquí coinciden con las claves de 'operaciones'
            '1': "Suma",
            '2': "Resta",
            '3': "Multiplicación",
            '4': "División",
            '5': "Potencia",
            '6': "Raíz Cuadrada",
            '7': "Ver Historial",
            '8': "Salir"
        },
        'prompt_opcion': "Ingresa tu opción: ",
        'prompt_num_1': "Ingresa el primer número: ",
        'prompt_num_2': "Ingresa el segundo número: ",
        'prompt_num_unico': "Ingresa el número: ",
        'resultado': "El resultado es: ",
        'historial_titulo': "\n--- Historial de Cálculos ---",
        'historial_vacio': "El historial está vacío.",
        'despedida': "¡Hasta la próxima! 🚀",
        'error_opcion_invalida': "Opción no válida. Por favor, elige una del menú.",
        'error_valor_invalido': "Error: Entrada no válida. Ingresa solo números."
    }
}


# Introducción a funciones lambda para simplificar
# En el diccionario de arriba, he reemplazado las funciones simples
# (sumar, restar, etc.) con funciones 'lambda'. Son funciones anónimas
# y de una sola línea, perfectas para operaciones sencillas como estas.
# def sumar(a, b): return a + b  ES EQUIVALENTE A  lambda a, b: a + b

# --- LÓGICA DE LA APLICACIÓN ---
# El código de abajo ahora solo se encarga de la lógica,
# y obtiene todo el texto del diccionario 'configuracion'.

def calculadora_configurable(config):
    """
    Función principal que ejecuta la calculadora.
    Ahora recibe el diccionario de configuración como argumento.
    """
    historial = []
    textos = config['textos']
    operaciones = config['operaciones']

    while True:
        print(textos['titulo'])
        # Imprime el menú dinámicamente desde el diccionario
        for clave, valor in textos['menu_principal'].items():
            print(f"{clave}. {valor}")

        opcion = input(textos['prompt_opcion'])

        if opcion == '8':  # Salir
            print(textos['despedida'])
            break

        elif opcion == '7':  # Historial
            print(textos['historial_titulo'])
            if not historial:
                print(textos['historial_vacio'])
            else:
                for calculo in historial:
                    print(calculo)
            print("-" * (len(textos['historial_titulo']) - 1))
            continue

        if opcion in operaciones:
            try:
                op_info = operaciones[opcion]

                if op_info['num_args'] == 1:
                    num1 = float(input(textos['prompt_num_unico']))
                    resultado = op_info['funcion'](num1)
                    if not isinstance(resultado, str):
                        historial.append(f"√{num1} = {resultado:.2f}")
                else:
                    num1 = float(input(textos['prompt_num_1']))
                    num2 = float(input(textos['prompt_num_2']))
                    resultado = op_info['funcion'](num1, num2)
                    if not isinstance(resultado, str):
                        # Nota: el símbolo ya no está en el diccionario,
                        # podríamos agregarlo de nuevo o simplemente usar el texto
                        op_texto = op_info['texto']
                        historial.append(f"{num1} ({op_texto}) {num2} = {resultado:.2f}")

                print("-" * 30)
                print(f"{textos['resultado']}{resultado}")
                print("-" * 30)

            except ValueError:
                print(textos['error_valor_invalido'])
        else:
            print(textos['error_opcion_invalida'])


# Iniciar la calculadora pasándole la configuración
calculadora_configurable(configuracion)