"""Modelo de membresía de usuario."""

from __future__ import annotations

from dataclasses import dataclass

from biblioteca_digital import constantes
from biblioteca_digital.patrones.strategy.impl.multa_estandar_strategy import (
    MultaEstandarStrategy,
)
from biblioteca_digital.patrones.strategy.impl.multa_reducida_strategy import (
    MultaReducidaStrategy,
)
from biblioteca_digital.patrones.strategy.impl.sin_multa_strategy import SinMultaStrategy
from biblioteca_digital.patrones.strategy.multa_strategy import MultaStrategy

_ESTRATEGIAS: dict[str, MultaStrategy] = {
    constantes.TIPO_MEMBRESIA_BASICA: MultaEstandarStrategy(),
    constantes.TIPO_MEMBRESIA_ESTANDAR: MultaReducidaStrategy(),
    constantes.TIPO_MEMBRESIA_PREMIUM: SinMultaStrategy(),
}

_DIAS_PRESTAMO: dict[str, int] = {
    constantes.TIPO_MEMBRESIA_BASICA: 7,
    constantes.TIPO_MEMBRESIA_ESTANDAR: 14,
    constantes.TIPO_MEMBRESIA_PREMIUM: 30,
}


@dataclass(frozen=True)
class Membresia:
    """Representa una membresía con políticas de préstamo y multa."""

    tipo: str
    dias_prestamo: int
    estrategia_multa: MultaStrategy

    def calcular_multa(self, dias_retraso: int) -> float:
        return self.estrategia_multa.calcular_multa(dias_retraso)

    @classmethod
    def crear(cls, tipo: str) -> "Membresia":
        tipo_normalizado = tipo.capitalize()
        if tipo_normalizado not in _ESTRATEGIAS:
            raise ValueError(f"Tipo de membresía inválido: {tipo}")
        return cls(
            tipo=tipo_normalizado,
            dias_prestamo=_DIAS_PRESTAMO[tipo_normalizado],
            estrategia_multa=_ESTRATEGIAS[tipo_normalizado],
        )

    def __str__(self) -> str:
        return self.tipo


__all__ = ["Membresia"]
