"""
Entidad Reserva del sistema.
Representa una reserva de un material no disponible.
"""

from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from biblioteca_digital.entidades.usuarios.usuario import Usuario
    from biblioteca_digital.entidades.materiales.material import Material

from biblioteca_digital.constantes import ESTADO_RESERVA_PENDIENTE


class Reserva:
    """
    Representa una reserva de un material que está prestado.
    Permite a usuarios esperar por materiales no disponibles.
    """

    _contador_id = 0

    def __init__(self, usuario: 'Usuario', material: 'Material', fecha_reserva: date):
        """
        Inicializa una reserva.

        Args:
            usuario: Usuario que realiza la reserva
            material: Material reservado
            fecha_reserva: Fecha de la reserva
        """
        Reserva._contador_id += 1
        self._id_reserva = Reserva._contador_id
        self._usuario = usuario
        self._material = material
        self._fecha_reserva = fecha_reserva
        self._estado = ESTADO_RESERVA_PENDIENTE

    def get_id(self) -> int:
        """Retorna el ID de la reserva."""
        return self._id_reserva

    def get_usuario(self) -> 'Usuario':
        """Retorna el usuario de la reserva."""
        return self._usuario

    def get_material(self) -> 'Material':
        """Retorna el material reservado."""
        return self._material

    def get_fecha_reserva(self) -> date:
        """Retorna la fecha de reserva."""
        return self._fecha_reserva

    def get_estado(self) -> str:
        """Retorna el estado de la reserva."""
        return self._estado

    def set_estado(self, estado: str) -> None:
        """
        Establece el estado de la reserva.

        Args:
            estado: Nuevo estado
        """
        self._estado = estado

    def __str__(self) -> str:
        """Representación en string."""
        return f"Reserva #{self._id_reserva}: {self._material.get_titulo()} - {self._usuario.get_nombre()} [{self._estado}]"