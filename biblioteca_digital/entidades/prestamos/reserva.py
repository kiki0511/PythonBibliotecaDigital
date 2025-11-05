"""Entidad Reserva."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, TYPE_CHECKING

from biblioteca_digital import constantes

if TYPE_CHECKING:
    from biblioteca_digital.entidades.materiales.material import Material
    from biblioteca_digital.entidades.usuarios.usuario import Usuario


@dataclass
class Reserva:
    """Reserva de un material actualmente no disponible."""

    usuario: "Usuario"
    material: "Material"
    fecha_reserva: datetime = field(default_factory=datetime.now)
    estado: str = field(default=constantes.ESTADO_RESERVA_PENDIENTE, init=False)
    fecha_notificacion: Optional[datetime] = None

    def marcar_notificada(self, fecha: Optional[datetime] = None) -> None:
        self.estado = constantes.ESTADO_RESERVA_NOTIFICADA
        self.fecha_notificacion = fecha or datetime.now()

    def completar(self) -> None:
        self.estado = constantes.ESTADO_RESERVA_COMPLETADA

    def cancelar(self) -> None:
        self.estado = constantes.ESTADO_RESERVA_CANCELADA

    def esta_pendiente(self) -> bool:
        return self.estado == constantes.ESTADO_RESERVA_PENDIENTE


__all__ = ["Reserva"]
