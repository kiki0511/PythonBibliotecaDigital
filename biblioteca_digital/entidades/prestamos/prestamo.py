"""Entidad que representa un préstamo de material."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, TYPE_CHECKING

from biblioteca_digital import constantes

if TYPE_CHECKING:
    from biblioteca_digital.entidades.materiales.material import Material
    from biblioteca_digital.entidades.usuarios.usuario import Usuario


@dataclass
class Prestamo:
    """Registra el préstamo de un material a un usuario."""

    usuario: "Usuario"
    material: "Material"
    fecha_prestamo: datetime
    fecha_vencimiento: datetime
    fecha_devolucion: Optional[datetime] = None
    estado: str = field(init=False, default=constantes.ESTADO_PRESTAMO_ACTIVO)

    def __post_init__(self) -> None:
        if self.fecha_vencimiento <= self.fecha_prestamo:
            raise ValueError("La fecha de vencimiento debe ser posterior al préstamo.")

    def marcar_vencido(self) -> None:
        if self.estado == constantes.ESTADO_PRESTAMO_ACTIVO:
            self.estado = constantes.ESTADO_PRESTAMO_VENCIDO

    def registrar_devolucion(self, fecha: Optional[datetime] = None) -> None:
        if self.estado == constantes.ESTADO_PRESTAMO_DEVUELTO:
            return
        self.fecha_devolucion = fecha or datetime.now()
        self.estado = constantes.ESTADO_PRESTAMO_DEVUELTO
        self.material.marcar_disponible()
        self.usuario.cerrar_prestamo(self)

    def calcular_dias_retraso(self, referencia: Optional[datetime] = None) -> int:
        referencia = referencia or self.fecha_devolucion or datetime.now()
        if referencia <= self.fecha_vencimiento:
            return 0
        delta = referencia.date() - self.fecha_vencimiento.date()
        return max(0, delta.days)

    def esta_activo(self) -> bool:
        return self.estado == constantes.ESTADO_PRESTAMO_ACTIVO

    def esta_vencido(self) -> bool:
        if self.estado == constantes.ESTADO_PRESTAMO_VENCIDO:
            return True
        if self.estado == constantes.ESTADO_PRESTAMO_ACTIVO:
            if datetime.now() > self.fecha_vencimiento:
                self.marcar_vencido()
                return True
        return False

    def __str__(self) -> str:
        return (
            f"{self.material.titulo} - {self.usuario.nombre} "
            f"(Vence: {self.fecha_vencimiento.date()})"
        )


__all__ = ["Prestamo"]
