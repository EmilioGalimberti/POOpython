# equipo.py

class Equipo:
    """
    Representa a un equipo de fútbol y almacena sus estadísticas en un campeonato.
    """

    def __init__(self, nombre):
        """
        Constructor de la clase Equipo.
        Inicializa el nombre y todas las estadísticas en cero.
        """
        self.nombre = nombre

        # Inicialización de todas las estadísticas
        self.partidos_jugados = 0
        self.partidos_jugados_local = 0
        self.partidos_jugados_visitante = 0
        self.goles_a_favor = 0
        self.goles_en_contra = 0
        self.partidos_ganados = 0
        self.partidos_empatados = 0
        self.partidos_perdidos = 0
        self.puntos = 0

    @property
    def diferencia_goles(self):
        """
        Calcula y devuelve la diferencia total de goles.
        Es una propiedad calculada, no se almacena directamente.
        """
        return self.goles_a_favor - self.goles_en_contra

    def registrar_partido(self, partido):
        """
        Actualiza las estadísticas del equipo basándose en el resultado de un partido.
        """
        self.partidos_jugados += 1

        # Determinar si el equipo fue local o visitante para sumar goles
        if self == partido.equipo_local:
            self.partidos_jugados_local += 1
            self.goles_a_favor += partido.goles_local
            self.goles_en_contra += partido.goles_visitante
        else:  # Fue visitante
            self.partidos_jugados_visitante += 1
            self.goles_a_favor += partido.goles_visitante
            self.goles_en_contra += partido.goles_local

        # Determinar resultado para sumar puntos y estadísticas de G/E/P
        ganador = partido.get_ganador()
        if ganador is None:  # Hubo empate
            self.partidos_empatados += 1
            self.puntos += 1
        elif ganador == self:  # El equipo ganó
            self.partidos_ganados += 1
            self.puntos += 3
        else:  # El equipo perdió
            self.partidos_perdidos += 1
            # No se suman puntos por perder

    def mostrar_estadisticas(self):
        """
        Imprime en la consola un resumen de las estadísticas del equipo.
        """
        print(f"--- Estadísticas de: {self.nombre} ---")
        print(
            f"Partidos Jugados: {self.partidos_jugados} ({self.partidos_jugados_local} Local / {self.partidos_jugados_visitante} Visitante)")
        print(f"Victorias: {self.partidos_ganados}")
        print(f"Empates: {self.partidos_empatados}")
        print(f"Derrotas: {self.partidos_perdidos}")
        print(f"Goles a Favor: {self.goles_a_favor}")
        print(f"Goles en Contra: {self.goles_en_contra}")
        print(f"Diferencia de Goles: {self.diferencia_goles}")
        print(f"Puntos Totales: {self.puntos}")
        print("-" * (23 + len(self.nombre)))