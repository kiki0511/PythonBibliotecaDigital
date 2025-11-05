"""Interfaz para las estrategias de cálculo de multas."""

from __future__ import annotations

from abc import ABC, abstractmethod


class MultaStrategy(ABC):
    """Define la operación para calcular multas por retraso."""

    @abstractmethod
    def calcular_multa(self, dias_retraso: int) -> float:
        """Devuelve el monto total de la multa para los días indicados."""
        raise NotImplementedError


__all__ = ["MultaStrategy"]
