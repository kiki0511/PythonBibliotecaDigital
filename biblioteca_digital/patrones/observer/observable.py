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
