from datetime import date
from dominio.empleado import EmpleadoMensual, EmpleadoPorHora
from dominio.departamento import Departamento
from dominio.registro_tiempo import RegistroTiempo

if __name__ == "__main__":
    desarrollo = Departamento("Desarrollo de Software")

    # Instanciación de empleados
    ana = EmpleadoMensual("Ana Torres", "ana.torres@ecotech.cl", 1200000.0)
    carlos = EmpleadoPorHora("Carlos Gómez", "carlos.gomez@ecotech.cl", horas=160, valor_hora=8500.0)

    desarrollo.agregar_empleado(ana)
    desarrollo.agregar_empleado(carlos)

    # Creación de registros de tiempo
    reg1 = RegistroTiempo(fecha=date(2026, 9, 1), horas=8.0, empleado=ana, proyecto="Panel Solar EcoTech")
    reg2 = RegistroTiempo(fecha=date(2026, 9, 2), horas=6.5, empleado=ana, proyecto="Optimización Energética")
    reg3 = RegistroTiempo(fecha=date(2026, 9, 1), horas=8.0, empleado=carlos, proyecto="Panel Solar EcoTech")

    # Asociar registros a cada empleado
    ana.registrar_horas(reg1)
    ana.registrar_horas(reg2)
    carlos.registrar_horas(reg3)

    # Mostrar la relación en consola
    print("--- Registros de Tiempo EcoTech ---")
    print(reg1.mostrar_detalle())
    print(reg2.mostrar_detalle())
    print(reg3.mostrar_detalle())

    print("\n--- Horas Acumuladas por Empleado ---")
    print(f"{ana.nombre}: {ana.total_horas_registradas()} hrs totales.")
    print(f"{carlos.nombre}: {carlos.total_horas_registradas()} hrs totales.")