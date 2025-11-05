"""
Archivo integrador generado automaticamente
Directorio: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/patrones/singleton
Fecha: 2025-11-05 09:05:45
Total de archivos integrados: 1
"""

# ================================================================================
# ARCHIVO 1/1: singleton_meta.py
# Ruta: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/patrones/singleton/singleton_meta.py
# ================================================================================

"""Metaclase para implementar el patrón Singleton thread-safe."""

from __future__ import annotations

from threading import RLock
from typing import Any, Dict, Type


class SingletonMeta(type):
    """Metaclase que garantiza una única instancia por clase."""

    _instances: Dict[Type, Any] = {}
    _lock: RLock = RLock()

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


__all__ = ["SingletonMeta"]


