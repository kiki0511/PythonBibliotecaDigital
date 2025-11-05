"""
Archivo integrador generado automaticamente
Directorio: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/patrones/observer
Fecha: 2025-11-05 09:05:45
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: observable.py
# Ruta: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/patrones/observer/observable.py
# ================================================================================

"""Implementación base del patrón Observable."""

from __future__ import annotations

from typing import Generic, List, TypeVar

from .observer import Observer

T = TypeVar("T")


class Observable(Generic[T]):
    """Gestiona la suscripción de observadores y notificaciones."""

    def __init__(self) -> None:
        self._observadores: List[Observer[T]] = []

    def agregar_observador(self, observador: Observer[T]) -> None:
        if observador not in self._observadores:
            self._observadores.append(observador)

    def remover_observador(self, observador: Observer[T]) -> None:
        if observador in self._observadores:
            self._observadores.remove(observador)

    def notificar(self, evento: T) -> None:
        for observador in list(self._observadores):
            observador.actualizar(evento)


__all__ = ["Observable"]


# ================================================================================
# ARCHIVO 2/2: observer.py
# Ruta: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/patrones/observer/observer.py
# ================================================================================

"""Interfaz del patrón Observer."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class Observer(ABC, Generic[T]):
    """Define la interfaz que deben implementar los observadores."""

    @abstractmethod
    def actualizar(self, evento: T) -> None:
        """Recibe una notificación con el evento emitido."""
        raise NotImplementedError


__all__ = ["Observer"]


