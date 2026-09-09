from datetime import date

class Empleado:
    def __init__(self, nombre: str, correo: str):
        self.nombre = nombre
        self.correo = correo
        self._registros: list = []  # Colección para multiplicidad 0..*

    def registrar_horas(self, registro) -> None:
        self._registros.append(registro)

    def total_horas_registradas(self) -> float:
        return sum(reg.horas for reg in self._registros)

    def mostrar_datos(self) -> str:
        return f"{self.nombre} - {self.correo}"

    def calcular_pago(self) -> float:
        raise NotImplementedError("Cada tipo de empleado debe implementar calcular_pago")


class EmpleadoMensual(Empleado):
    def __init__(self, nombre: str, correo: str, sueldo: float):
        super().__init__(nombre, correo)
        self.sueldo = sueldo

    def calcular_pago(self) -> float:
        return self.sueldo


class EmpleadoPorHora(Empleado):
    def __init__(self, nombre: str, correo: str, horas: float, valor_hora: float):
        super().__init__(nombre, correo)
        self.horas = horas
        self.valor_hora = valor_hora

    def calcular_pago(self) -> float:
        return self.horas * self.valor_hora