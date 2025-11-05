"""Estrategia de multa reducida para membresías estándar."""

from __future__ import annotations

from biblioteca_digital.constantes import MULTA_ESTANDAR_POR_DIA

from ..multa_strategy import MultaStrategy


class MultaReducidaStrategy(MultaStrategy):
    """Aplica una multa menor para clientes con membresía estándar."""

    def calcular_multa(self, dias_retraso: int) -> float:
        return max(0, dias_retraso) * MULTA_ESTANDAR_POR_DIA


__all__ = ["MultaReducidaStrategy"]
