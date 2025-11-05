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
