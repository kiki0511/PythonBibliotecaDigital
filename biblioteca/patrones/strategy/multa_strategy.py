"""
Interfaz para estrategias de cálculo de multas.
Implementa patrón Strategy.
"""

from abc import ABC, abstractmethod


class MultaStrategy(ABC):
    """
    Interfaz para estrategias de cálculo de multas.
    Cada tipo de membresía usa una estrategia diferente.
    """

    @abstractmethod
    def calcular_multa(self, dias_retraso: int) -> float:
        """
        Calcula la multa por días de retraso.

        Args:
            dias_retraso: Número de días de retraso

        Returns:
            Monto de la multa en pesos
        """
        pass