"""
Archivo integrador generado automaticamente
Directorio: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/patrones/strategy
Fecha: 2025-11-05 09:05:45
Total de archivos integrados: 1
"""

# ================================================================================
# ARCHIVO 1/1: multa_strategy.py
# Ruta: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/patrones/strategy/multa_strategy.py
# ================================================================================

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


