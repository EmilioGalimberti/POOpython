# partido.py
# No es necesario importar la clase Equipo si los archivos se ejecutan juntos,
# pero es una buena práctica si estuvieran en módulos separados.

class Partido:
    """
    Representa un partido de fútbol entre un equipo local y uno visitante.
    """
    def __init__(self, equipo_local, equipo_visitante, goles_local, goles_visitante):
        """
        Constructor de la clase Partido.
        Almacena los equipos, los goles y automáticamente registra el partido
        en ambos equipos.
        """
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.goles_local = goles_local
        self.goles_visitante = goles_visitante

        # ¡Importante! Notificamos a ambos equipos sobre este partido
        self.equipo_local.registrar_partido(self)
        self.equipo_visitante.registrar_partido(self)

    def hay_empate(self):
        """Devuelve True si el partido terminó en empate, False en caso contrario."""
        return self.goles_local == self.goles_visitante

    def get_ganador(self):
        """
        Devuelve el objeto Equipo que ganó el partido.
        Si hay empate, devuelve None.
        """
        if self.hay_empate():
            return None
        elif self.goles_local > self.goles_visitante:
            return self.equipo_local
        else:
            return self.equipo_visitante