"""Estrategia de multa estándar para membresías básicas."""

from __future__ import annotations

from biblioteca_digital.constantes import MULTA_BASICA_POR_DIA

from ..multa_strategy import MultaStrategy


class MultaEstandarStrategy(MultaStrategy):
    """Aplica la multa fija por día configurada para membresía básica."""

    def calcular_multa(self, dias_retraso: int) -> float:
        return max(0, dias_retraso) * MULTA_BASICA_POR_DIA


__all__ = ["MultaEstandarStrategy"]
