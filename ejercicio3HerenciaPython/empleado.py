# empleados.py
from abc import ABC, abstractmethod

class Empleado(ABC):
    """
    Clase base abstracta para todos los tipos de empleados.
    Define la estructura común y un método abstracto para el cálculo del sueldo.
    """
    def __init__(self, legajo, nombre, apellido, sueldo_basico):
        self._legajo = int(legajo)
        self._nombre = nombre
        self._apellido = apellido
        self._sueldo_basico = float(sueldo_basico)

    @property
    def legajo(self):
        return self._legajo

    @property
    def nombre_completo(self):
        return f"{self._nombre} {self._apellido}"

    @abstractmethod
    def calcular_sueldo(self):
        """
        Método abstracto. Cada subclase DEBE implementar su propia
        lógica para calcular el sueldo final.
        """
        pass

    def __str__(self):
        return f"Legajo: {self.legajo} - {self.nombre_completo}"


class Obrero(Empleado):
    """Representa a un empleado de tipo Obrero."""
    def __init__(self, legajo, nombre, apellido, sueldo_basico, dias_trabajados):
        super().__init__(legajo, nombre, apellido, sueldo_basico)
        self._dias_trabajados = int(dias_trabajados)

    def calcular_sueldo(self):
        """Calcula el sueldo proporcional a los días trabajados."""
        sueldo_por_dia = self._sueldo_basico / 20
        return sueldo_por_dia * self._dias_trabajados


class Administrativo(Empleado):
    """Representa a un empleado de tipo Administrativo."""
    def __init__(self, legajo, nombre, apellido, sueldo_basico, presentismo):
        super().__init__(legajo, nombre, apellido, sueldo_basico)
        # Convertimos 'S'/'N' a un valor booleano (True/False)
        self._cobra_presentismo = (presentismo.upper() == 'S')

    def calcular_sueldo(self):
        """Aplica un 13% de aumento si corresponde el presentismo."""
        if self._cobra_presentismo:
            return self._sueldo_basico * 1.13
        return self._sueldo_basico


class Vendedor(Empleado):
    """Representa a un empleado de tipo Vendedor."""
    def __init__(self, legajo, nombre, apellido, sueldo_basico, total_ventas):
        super().__init__(legajo, nombre, apellido, sueldo_basico)
        self._total_ventas = float(total_ventas)

    def calcular_sueldo(self):
        """Calcula el sueldo básico más un 1% de comisión por ventas."""
        comision = self._total_ventas * 0.01
        return self._sueldo_basico + comision