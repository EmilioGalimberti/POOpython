# main.py
from equipo import Equipo
from partido import Partido

# 1. Creamos las instancias de los equipos
equipo_a = Equipo("Leones del Norte")
equipo_b = Equipo("Tigres del Sur")
equipo_c = Equipo("Águilas del Centro")

# Lista para acceder fácilmente a todos los equipos
equipos = [equipo_a, equipo_b, equipo_c]

# 2. Registramos los partidos del campeonato
print("⚽ Registrando partidos del campeonato...\n")
Partido(equipo_a, equipo_b, 2, 1) # Gana A
Partido(equipo_b, equipo_c, 3, 3) # Empatan B y C
Partido(equipo_c, equipo_a, 0, 1) # Gana A
Partido(equipo_b, equipo_a, 0, 2) # Gana A
Partido(equipo_c, equipo_b, 1, 0) # Gana C
Partido(equipo_a, equipo_c, 2, 2) # Empatan A y C

# 3. Mostramos las estadísticas finales de cada equipo
print("📊 Resultados finales del campeonato:\n")
for equipo in equipos:
    equipo.mostrar_estadisticas()