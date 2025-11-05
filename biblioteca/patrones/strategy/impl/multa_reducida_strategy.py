"""
Estrategia de multa reducida para membresía Estándar.
"""

from biblioteca_digital.patrones.strategy.multa_strategy import MultaStrategy
from biblioteca_digital.constantes import MULTA_ESTANDAR_POR_DIA


class MultaReducidaStrategy(MultaStrategy):
    """
    Estrategia de multa para membresía Estándar.
    Aplica multa reducida de 1.00 por día de retraso.
    """

    def calcular_multa(self, dias_retraso: int) -> float:
        """
        Calcula multa reducida.

        Args:
            dias_retraso: Días de retraso

        Returns:
            Multa total (dias * 1.00)
        """
        if dias_retraso <= 0:
            return 0.0
        return float(dias_retraso * MULTA_ESTANDAR_POR_DIA)