from dataclasses import dataclass
from datetime import date

TIPOS_ATENCION = ("Extracción", "Limpieza", "Diagnóstico", "Calzas", "Control")
PRIORIDADES = ("Urgente", "Normal", "Control")


@dataclass
class Cita:
    cliente: str
    cedula: str
    tipo_atencion: str
    prioridad: str
    fecha: date
    cantidad: int = 1

    def __str__(self) -> str:
        return (
            f"{self.fecha.strftime('%d/%m/%Y')} | {self.cliente} (CC {self.cedula}) | "
            f"{self.tipo_atencion} | Prioridad: {self.prioridad} | Cantidad: {self.cantidad}"
        )
