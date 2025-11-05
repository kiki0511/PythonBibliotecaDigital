"""
Servicio de gestión de préstamos.
"""

from datetime import date
from typing import Optional
from biblioteca_digital.entidades.prestamos.prestamo import Prestamo
from biblioteca_digital.entidades.usuarios.usuario import Usuario
from biblioteca_digital.entidades.materiales.material import Material
from biblioteca_digital.excepciones.material_no_disponible_exception import MaterialNoDisponibleException
from biblioteca_digital.servicios.materiales.material_service_registry import MaterialServiceRegistry
from biblioteca_digital.constantes import (
    ESTADO_MATERIAL_PRESTADO,
    ESTADO_MATERIAL_DISPONIBLE,
    ESTADO_PRESTAMO_DEVUELTO
)


class PrestamoService:
    """
    Servicio para gestionar préstamos de materiales.
    """

    def __init__(self):
        """Inicializa el servicio de préstamos."""
        self._registry = MaterialServiceRegistry.get_instance()

    def realizar_prestamo(
        self,
        usuario: Usuario,
        material: Material
    ) -> Prestamo:
        """
        Realiza un préstamo de material a un usuario.

        Args:
            usuario: Usuario que solicita el préstamo
            material: Material a prestar

        Returns:
            Préstamo creado

        Raises:
            MaterialNoDisponibleException: Si el material no está disponible
        """
        if not material.esta_disponible():
            raise MaterialNoDisponibleException(
                material.get_id_material(),
                material.get_titulo()
            )

        dias_prestamo = self._registry.obtener_dias_prestamo(material)

        prestamo = Prestamo(
            usuario=usuario,
            material=material,
            fecha_prestamo=date.today(),
            dias_prestamo=dias_prestamo
        )

        material.set_estado(ESTADO_MATERIAL_PRESTADO)

        return prestamo

    def devolver_material(self, prestamo: Prestamo) -> float:
        """
        Registra la devolución de un material.

        Args:
            prestamo: Préstamo a devolver

        Returns:
            Multa generada (si hay retraso)
        """
        prestamo.set_fecha_devolucion(date.today())
        prestamo.set_estado(ESTADO_PRESTAMO_DEVUELTO)
        prestamo.get_material().set_estado(ESTADO_MATERIAL_DISPONIBLE)

        dias_retraso = prestamo.calcular_dias_retraso()
        multa = prestamo.get_usuario().calcular_multa(dias_retraso)

        return multa