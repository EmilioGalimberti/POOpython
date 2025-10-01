# Simulador de Ruleta
Desarrollar un programa que simule el juego de la ruleta.  

Para ello generar al azar 1000 tiradas y luego informar:

* Cantidad de pares e impares 
* Cantidad de tiradas por cada docena 
* Porcentaje de ceros sobre el total de jugadas. 
* Cantidad de rojos y de negros



----------------------------------------
# main2
Deje los dos main solo para guardar dos tipos de soluciones, 
Esta seguna solucion utiliza diccionarios y el siguiente calculo para optimizar:    
## Propuesta de Optimización
Podemos eliminar la cadena de if/elif/elif para las docenas usando un cálculo matemático. Si a cualquier número (del 1 al 36) le restamos 1 y lo dividimos de forma entera por 12, obtendremos un índice: 0 para la primera docena, 1 para la segunda y 2 para la tercera.

(1 a 12) - 1 → (0 a 11) // 12 → 0

(13 a 24) - 1 → (12 a 23) // 12 → 1

(25 a 36) - 1 → (24 a 35) // 12 → 2

Podemos usar este índice para actualizar los contadores de docenas guardados en una lista.