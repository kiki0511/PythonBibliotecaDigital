"""
Estrategia sin multa para membresía Premium.
"""

from biblioteca_digital.patrones.strategy.multa_strategy import MultaStrategy


class SinMultaStrategy(MultaStrategy):
    """
    Estrategia de multa para membresía Premium.
    No aplica multas sin importar los días de retraso.
    """

    def calcular_multa(self, dias_retraso: int) -> float:
        """
        Calcula multa (siempre 0 para Premium).

        Args:
            dias_retraso: Días de retraso (no se usa)

        Returns:
            0.0 siempre
        """
        return 0.0