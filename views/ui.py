from core import validators as v
from core.engine import Engine
from models.cita import Cita


def _capturar_cita() -> Cita:
    print("\n--- Registrar cita ---")
    cliente = v.pedir_nombre()
    cedula = v.pedir_cedula()
    tipo = v.pedir_tipo()
    prioridad = v.pedir_prioridad()
    fecha = v.pedir_fecha()
    # Regla de negocio (heredada de la Actividad N.° 1):
    # Limpieza y Diagnóstico siempre atienden una sola unidad.
    cantidad = 1 if tipo in ("Limpieza", "Diagnóstico") else v.pedir_cantidad()
    return Cita(cliente=cliente, cedula=cedula, tipo_atencion=tipo,
                prioridad=prioridad, fecha=fecha, cantidad=cantidad)


def menu() -> None:
    engine = Engine()
    while True:
        print("\n===== CONSULTORIO ODONTOLÓGICO =====")
        print("1. Registrar cita")
        print("2. Informe de pila de urgencias (Extracción + Urgente)")
        print("3. Generar agenda del día (Cola de atención)")
        print("4. Atender siguiente cliente de la cola")
        print("5. Listar todas las citas")
        print("0. Salir")
        opcion = v.pedir_opcion_menu(5)

        if opcion == 1:
            try:
                engine.registrar_cita(_capturar_cita())
                print("✔ Cita registrada.")
            except ValueError as e:
                print(f"  ⚠ {e}")
        elif opcion == 2:
            informe = engine.listar_urgentes()
            if not informe:
                print("Sin clientes urgentes pendientes.")
            else:
                print("\nPILA DE URGENCIAS (más cercana primero):")
                for i, c in enumerate(informe, 1):
                    print(f"  {i}. {c}")
        elif opcion == 3:
            print("Generar agenda para el día:")
            dia = v.pedir_fecha()
            cola = engine.construir_cola_del_dia(dia)
            if cola.esta_vacia():
                print("No hay citas ese día.")
            else:
                print(f"\nAGENDA {dia.strftime('%d/%m/%Y')} ({len(cola)} clientes):")
                for i, c in enumerate(cola, 1):
                    print(f"  {i}. {c}")
                _atender_cola(cola)
        elif opcion == 4:
            dia = v.pedir_fecha()
            cola = engine.construir_cola_del_dia(dia)
            _atender_cola(cola)
        elif opcion == 5:
            if not engine.citas:
                print("No hay citas registradas.")
            for c in engine.citas:
                print(f"  - {c}")
        elif opcion == 0:
            print("¡Hasta luego!")
            break


def _atender_cola(cola) -> None:
    if cola.esta_vacia():
        print("No hay clientes en la cola.")
        return
    while not cola.esta_vacia() and v.pedir_si_no("¿Atender siguiente cliente?") == "s":
        atendido = cola.desencolar()
        print(f"▶ Atendiendo: {atendido}")
    print("Fin de la atención de la cola.")
