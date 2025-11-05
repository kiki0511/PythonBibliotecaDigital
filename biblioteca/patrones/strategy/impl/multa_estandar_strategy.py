"""
Estrategia de multa estándar para membresía Básica.
"""

from biblioteca_digital.patrones.strategy.multa_strategy import MultaStrategy
from biblioteca_digital.constantes import MULTA_BASICA_POR_DIA


class MultaEstandarStrategy(MultaStrategy):
    """
    Estrategia de multa para membresía Básica.
    Aplica multa estándar de 2.00 por día de retraso.
    """

    def calcular_multa(self, dias_retraso: int) -> float:
        """
        Calcula multa estándar.

        Args:
            dias_retraso: Días de retraso

        Returns:
            Multa total (dias * 2.00)
        """
        if dias_retraso <= 0:
            return 0.0
        return float(dias_retraso * MULTA_BASICA_POR_DIA)