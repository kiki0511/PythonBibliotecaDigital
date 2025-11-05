"""
Entidad Préstamo del sistema.
Representa un préstamo de material a un usuario.
"""

from datetime import date, timedelta
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from biblioteca_digital.entidades.usuarios.usuario import Usuario
    from biblioteca_digital.entidades.materiales.material import Material

from biblioteca_digital.constantes import ESTADO_PRESTAMO_ACTIVO


class Prestamo:
    """
    Representa un préstamo de un material a un usuario.
    Controla fechas de préstamo, vencimiento y devolución.
    """

    _contador_id = 0

    def __init__(
        self,
        usuario: 'Usuario',
        material: 'Material',
        fecha_prestamo: date,
        dias_prestamo: int
    ):
        """
        Inicializa un préstamo.

        Args:
            usuario: Usuario que realiza el préstamo
            material: Material prestado
            fecha_prestamo: Fecha en que se realiza el préstamo
            dias_prestamo: Días permitidos de préstamo

        Raises:
            ValueError: Si dias_prestamo es inválido
        """
        if dias_prestamo <= 0:
            raise ValueError("Los días de préstamo deben ser mayores a cero")

        Prestamo._contador_id += 1
        self._id_prestamo = Prestamo._contador_id
        self._usuario = usuario
        self._material = material
        self._fecha_prestamo = fecha_prestamo
        self._fecha_vencimiento = fecha_prestamo + timedelta(days=dias_prestamo)
        self._fecha_devolucion: Optional[date] = None
        self._estado = ESTADO_PRESTAMO_ACTIVO

    def get_id_prestamo(self) -> int:
        """Retorna el ID del préstamo."""
        return self._id_prestamo

    def get_usuario(self) -> 'Usuario':
        """Retorna el usuario del préstamo."""
        return self._usuario

    def get_material(self) -> 'Material':
        """Retorna el material prestado."""
        return self._material

    def get_fecha_prestamo(self) -> date:
        """Retorna la fecha de préstamo."""
        return self._fecha_prestamo

    def get_fecha_vencimiento(self) -> date:
        """Retorna la fecha de vencimiento."""
        return self._fecha_vencimiento

    def get_fecha_devolucion(self) -> Optional[date]:
        """Retorna la fecha de devolución real (None si no se devolvió)."""
        return self._fecha_devolucion

    def set_fecha_devolucion(self, fecha: date) -> None:
        """
        Establece la fecha de devolución.

        Args:
            fecha: Fecha de devolución
        """
        self._fecha_devolucion = fecha

    def get_estado(self) -> str:
        """Retorna el estado del préstamo."""
        return self._estado

    def set_estado(self, estado: str) -> None:
        """
        Establece el estado del préstamo.

        Args:
            estado: Nuevo estado
        """
        self._estado = estado

    def calcular_dias_retraso(self) -> int:
        """
        Calcula los días de retraso en la devolución.

        Returns:
            Número de días de retraso (0 si no hay retraso o aún no se devolvió)
        """
        if self._fecha_devolucion is None:
            fecha_referencia = date.today()
        else:
            fecha_referencia = self._fecha_devolucion

        if fecha_referencia > self._fecha_vencimiento:
            dias = (fecha_referencia - self._fecha_vencimiento).days
            return dias
        return 0

    def esta_vencido(self) -> bool:
        """
        Verifica si el préstamo está vencido.

        Returns:
            True si está vencido, False en caso contrario
        """
        return date.today() > self._fecha_vencimiento and self._fecha_devolucion is None

    def __str__(self) -> str:
        """Representación en string."""
        return f"Préstamo #{self._id_prestamo}: {self._material.get_titulo()} - {self._usuario.get_nombre()} (Vence: {self._fecha_vencimiento})"