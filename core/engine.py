from __future__ import annotations

from datetime import date

from models.cita import Cita
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

    def marcar_atendida(self, cita: Cita) -> None:
        """Marca una cita como atendida para que no vuelva a la agenda."""
        cita.atendida = True

    # --- Regla de negocio: Cola de urgencias ---
    def construir_cola_urgencias(self) -> Cola:
        """Solo Extracción + Urgente y aún no atendidas. Se encolan de la fecha más
        cercana a la más lejana, de modo que al desencolar se atienda primero la más
        cercana (FIFO sobre la agenda de urgencias)."""
        candidatas = [
            c for c in self._citas
            if c.tipo_atencion == "Extracción" and c.prioridad == "Urgente" and not c.atendida
        ]
        candidatas.sort(key=lambda c: c.fecha)
        cola = Cola()
        for c in candidatas:
            cola.encolar(c)
        return cola

    # --- Regla de negocio: Cola de atención diaria ---
    def construir_cola_del_dia(self, dia: date) -> Cola:
        """Agenda en el estricto orden de registro, sin las citas ya atendidas."""
        cola = Cola()
        for c in self._citas:
            if c.fecha == dia and not c.atendida:
                cola.encolar(c)
        return cola

    def listar_urgentes(self) -> list[Cita]:
        """Devuelve las urgencias ordenadas de la más cercana a la más lejana
        (frente de la cola hacia el final)."""
        cola = self.construir_cola_urgencias()
        return list(cola)
