"""
Archivo integrador generado automaticamente
Directorio: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/patrones/strategy/impl
Fecha: 2025-11-05 09:05:45
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: multa_estandar_strategy.py
# Ruta: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/patrones/strategy/impl/multa_estandar_strategy.py
# ================================================================================

"""Estrategia de multa estándar para membresías básicas."""

from __future__ import annotations

from biblioteca_digital.constantes import MULTA_BASICA_POR_DIA

from ..multa_strategy import MultaStrategy


class MultaEstandarStrategy(MultaStrategy):
    """Aplica la multa fija por día configurada para membresía básica."""

    def calcular_multa(self, dias_retraso: int) -> float:
        return max(0, dias_retraso) * MULTA_BASICA_POR_DIA


__all__ = ["MultaEstandarStrategy"]


# ================================================================================
# ARCHIVO 2/3: multa_reducida_strategy.py
# Ruta: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/patrones/strategy/impl/multa_reducida_strategy.py
# ================================================================================

"""Estrategia de multa reducida para membresías estándar."""

from __future__ import annotations

from biblioteca_digital.constantes import MULTA_ESTANDAR_POR_DIA

from ..multa_strategy import MultaStrategy


class MultaReducidaStrategy(MultaStrategy):
    """Aplica una multa menor para clientes con membresía estándar."""

    def calcular_multa(self, dias_retraso: int) -> float:
        return max(0, dias_retraso) * MULTA_ESTANDAR_POR_DIA


__all__ = ["MultaReducidaStrategy"]


# ================================================================================
# ARCHIVO 3/3: sin_multa_strategy.py
# Ruta: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/patrones/strategy/impl/sin_multa_strategy.py
# ================================================================================

"""Estrategia que representa ausencia de multas."""

from __future__ import annotations

from ..multa_strategy import MultaStrategy


class SinMultaStrategy(MultaStrategy):
    """Devuelve cero independientemente del retraso."""

    def calcular_multa(self, dias_retraso: int) -> float:
        return 0.0


__all__ = ["SinMultaStrategy"]


