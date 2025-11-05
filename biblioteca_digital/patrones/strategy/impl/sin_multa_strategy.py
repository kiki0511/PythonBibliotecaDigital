"""Estrategia que representa ausencia de multas."""

from __future__ import annotations

from ..multa_strategy import MultaStrategy


class SinMultaStrategy(MultaStrategy):
    """Devuelve cero independientemente del retraso."""

    def calcular_multa(self, dias_retraso: int) -> float:
        return 0.0


__all__ = ["SinMultaStrategy"]
