"""Servicios base para operaciones sobre materiales."""

from __future__ import annotations

from abc import ABC
from datetime import datetime, timedelta
from typing import Optional, TYPE_CHECKING

from biblioteca_digital.excepciones.material_no_disponible_exception import (
    MaterialNoDisponibleException,
)

if TYPE_CHECKING:
    from biblioteca_digital.entidades.materiales.material import Material
    from biblioteca_digital.entidades.usuarios.membresia import Membresia


class MaterialService(ABC):
    """Servicio base reutilizable por los distintos tipos de materiales."""

    def __init__(self, dias_prestamo_base: int) -> None:
        self._dias_prestamo_base = dias_prestamo_base

    def validar_disponibilidad(self, material: "Material") -> None:
        if not material.esta_disponible():
            raise MaterialNoDisponibleException(material.codigo)

    def calcular_fecha_vencimiento(
        self,
        material: "Material",
        membresia: Optional["Membresia"],
        fecha_referencia: Optional[datetime] = None,
    ) -> datetime:
        dias = self.calcular_dias_prestamo(membresia)
        fecha_referencia = fecha_referencia or datetime.now()
        return fecha_referencia + timedelta(days=dias)

    def calcular_dias_prestamo(self, membresia: Optional["Membresia"]) -> int:
        if membresia:
            return min(self._dias_prestamo_base, membresia.dias_prestamo)
        return self._dias_prestamo_base

    def prestar(self, material: "Material") -> None:
        self.validar_disponibilidad(material)
        material.marcar_prestado()

    def devolver(self, material: "Material") -> None:
        material.marcar_disponible()

    def descripcion(self, material: "Material") -> str:
        return material.descripcion_detallada()


__all__ = ["MaterialService"]
