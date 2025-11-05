"""
Interfaz Observer del patrón Observer.
Implementa tipo-seguridad con Generics.
"""

from typing import Generic, TypeVar
from abc import ABC, abstractmethod

T = TypeVar('T')


class Observer(Generic[T], ABC):
    """
    Interfaz Observer genérica.
    Los observadores concretos deben implementar actualizar().
    """

    @abstractmethod
    def actualizar(self, evento: T) -> None:
        """
        Método llamado cuando el observable notifica un cambio.

        Args:
            evento: Evento notificado (tipo genérico T)
        """
        pass