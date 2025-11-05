"""
Servicio de gestión de reservas.
"""

from datetime import date
from biblioteca_digital.entidades.prestamos.reserva import Reserva
from biblioteca_digital.entidades.usuarios.usuario import Usuario
from biblioteca_digital.entidades.materiales.material import Material
from biblioteca_digital.excepciones.biblioteca_exception import BibliotecaException


class ReservaService:
    """
    Servicio para gestionar reservas de materiales.
    """

    def crear_reserva(
        self,
        usuario: Usuario,
        material: Material
    ) -> Reserva:
        """
        Crea una reserva para un material.

        Args:
            usuario: Usuario que reserva
            material: Material a reservar

        Returns:
            Reserva creada

        Raises:
            BibliotecaException: Si el material está disponible
        """
        if material.esta_disponible():
            raise BibliotecaException(
                "No se puede reservar un material disponible. "
                "Puede realizar el préstamo directamente."
            )

        reserva = Reserva(
            usuario=usuario,
            material=material,
            fecha_reserva=date.today()
        )

        return reserva