from datetime import date
from dominio.empleado import Empleado

class RegistroTiempo:
    def __init__(self, fecha: date, horas: float, empleado: Empleado, proyecto: str = "General"):
        if horas <= 0:
            raise ValueError("Las horas trabajadas deben ser mayores a 0.")
        self.fecha = fecha
        self.horas = horas
        self.empleado = empleado
        self.proyecto = proyecto

    def mostrar_detalle(self) -> str:
        return f"[{self.fecha}] {self.empleado.nombre} - {self.horas} hrs en '{self.proyecto}'"