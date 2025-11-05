"""
Entidad Notificación del sistema.
Representa una notificación a un usuario.
"""

from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from biblioteca_digital.entidades.usuarios.usuario import Usuario


class Notificacion:
    """
    Representa una notificación del sistema a un usuario.
    Usada en el patrón Observer.
    """

    def __init__(self, tipo: str, mensaje: str, usuario: 'Usuario'):
        """
        Inicializa una notificación.

        Args:
            tipo: Tipo de notificación (PRESTAMO, DEVOLUCION, etc.)
            mensaje: Mensaje de la notificación
            usuario: Usuario destinatario
        """
        self._tipo = tipo
        self._mensaje = mensaje
        self._usuario = usuario
        self._fecha_hora = datetime.now()

    def get_tipo(self) -> str:
        """Retorna el tipo de notificación."""
        return self._tipo

    def get_mensaje(self) -> str:
        """Retorna el mensaje."""
        return self._mensaje

    def get_usuario(self) -> 'Usuario':
        """Retorna el usuario destinatario."""
        return self._usuario

    def get_fecha_hora(self) -> datetime:
        """Retorna la fecha y hora de la notificación."""
        return self._fecha_hora

    def __str__(self) -> str:
        """Representación en string."""
        return f"[{self._tipo}] {self._mensaje}"