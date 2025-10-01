# persona.py

class Persona:
    """
    Representa a una persona con sus datos básicos:
    documento, nombre, apellido y edad.
    """
    def __init__(self, documento, nombre, apellido, edad):
        """
        Constructor de la clase Persona.
        Inicializa los atributos de la instancia.
        Los datos de documento y edad se convierten a números enteros.
        """
        # Usamos un guión bajo para indicar que estos atributos son "privados",
        # una práctica común del encapsulamiento para proteger los datos.
        self._documento = int(documento)
        self._nombre = nombre
        self._apellido = apellido
        self._edad = int(edad)

    # --- Métodos de consulta (Getters) ---
    # Estos métodos permiten acceder a los atributos de forma controlada,
    # que es un principio clave del encapsulamiento. [cite: 243]

    @property
    def documento(self):
        """Devuelve el documento de la persona."""
        return self._documento

    @property
    def nombre(self):
        """Devuelve el nombre de la persona."""
        return self._nombre

    @property
    def apellido(self):
        """Devuelve el apellido de la persona."""
        return self._apellido

    @property
    def edad(self):
        """Devuelve la edad de la persona."""
        return self._edad

    # --- Método Mágico __str__ ---
    # Este método especial define cómo se debe representar el objeto
    # como una cadena de texto, por ejemplo, al usar print(). [cite: 289]
    def __str__(self):
        """
        Devuelve una representación en formato de texto del objeto Persona.
        """
        return f"{self.apellido}, {self.nombre} (DNI: {self.documento}, Edad: {self.edad})"