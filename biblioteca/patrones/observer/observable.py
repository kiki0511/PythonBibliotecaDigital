"""
Clase Observable del patrón Observer.
Implementa tipo-seguridad con Generics.
"""

from typing import Generic, TypeVar, List
from abc import ABC

if __name__ != "__main__":
    from biblioteca_digital.patrones.observer.observer import Observer

T = TypeVar('T')


class Observable(Generic[T], ABC):
    """
    Clase Observable genérica.
    Mantiene lista de observadores y los notifica de cambios.
    """

    def __init__(self):
        """Inicializa la lista de observadores."""
        self._observadores: List[Observer[T]] = []

    def agregar_observador(self, observador: Observer[T]) -> None:
        """
        Agrega un observador a la lista.

        Args:
            observador: Observer a agregar
        """
        if observador not in self._observadores:
            self._observadores.append(observador)

    def eliminar_observador(self, observador: Observer[T]) -> None:
        """
        Elimina un observador de la lista.

        Args:
            observador: Observer a eliminar
        """
        if observador in self._observadores:
            self._observadores.remove(observador)

    def notificar_observadores(self, evento: T) -> None:
        """
        Notifica a todos los observadores suscritos.

        Args:
            evento: Evento a notificar (tipo genérico T)
        """
        for observador in self._observadores:
            observador.actualizar(evento)