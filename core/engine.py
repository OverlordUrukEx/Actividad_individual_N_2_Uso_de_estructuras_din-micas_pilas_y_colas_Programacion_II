from datetime import date

from models.cita import Cita
from core.pila import Pila
from core.cola import Cola


class Engine:
    """Motor de negocio: filtra, ordena y estructura las citas."""

    def __init__(self):
        self._citas: list[Cita] = []

    def registrar_cita(self, cita: Cita) -> None:
        if any(c.cedula == cita.cedula and c.fecha == cita.fecha for c in self._citas):
            raise ValueError("Ya existe una cita para esa cédula en esa fecha.")
        self._citas.append(cita)

    @property
    def citas(self) -> list[Cita]:
        return list(self._citas)

    # --- Regla de negocio: Pilas de urgencias ---
    def construir_pila_urgentes(self) -> Pila:
        """Solo Extracción + Urgente, ordenadas de la fecha más lejana a la más cercana,
        de modo que al desapilar quede la más cercana arriba (lista para llamar)."""
        candidatas = [
            c for c in self._citas
            if c.tipo_atencion == "Extracción" and c.prioridad == "Urgente"
        ]
        candidatas.sort(key=lambda c: c.fecha, reverse=True)
        pila = Pila()
        for c in candidatas:
            pila.apilar(c)
        return pila

    # --- Regla de negocio: Cola de atención diaria ---
    def construir_cola_del_dia(self, dia: date) -> Cola:
        """Agenda en el estricto orden de registro (orden en que se agendaron)."""
        cola = Cola()
        for c in self._citas:
            if c.fecha == dia:
                cola.encolar(c)
        return cola

    def listar_urgentes(self) -> list[Cita]:
        """Devuelve las urgencias ordenadas de la más cercana a la más lejana
        (cima de la pila hacia el fondo)."""
        pila = self.construir_pila_urgentes()
        return list(pila)
