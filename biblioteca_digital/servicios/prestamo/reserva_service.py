"""Servicio para gestionar reservas de materiales."""

from __future__ import annotations

from collections import defaultdict
from typing import Dict, List, Optional, TYPE_CHECKING

from biblioteca_digital.entidades.prestamos.reserva import Reserva
from biblioteca_digital.patrones.singleton.singleton_meta import SingletonMeta

if TYPE_CHECKING:
    from biblioteca_digital.entidades.materiales.material import Material
    from biblioteca_digital.entidades.usuarios.usuario import Usuario
    from biblioteca_digital.notificaciones.notificacion_service import NotificacionService


class ReservaService(metaclass=SingletonMeta):
    """Gestiona la cola de reservas por material."""

    def __init__(
        self, notificacion_service: Optional["NotificacionService"] = None
    ) -> None:
        self._reservas_por_material: Dict[str, List[Reserva]] = defaultdict(list)
        self._notificacion_service = notificacion_service

    @classmethod
    def get_instance(cls) -> "ReservaService":
        return cls()

    def crear_reserva(self, usuario: "Usuario", material: "Material") -> Reserva:
        reserva = Reserva(usuario=usuario, material=material)
        self._reservas_por_material[material.codigo].append(reserva)
        usuario.agregar_reserva(reserva)
        return reserva

    def cancelar_reserva(self, reserva: Reserva) -> None:
        codigo = reserva.material.codigo
        cola = self._reservas_por_material.get(codigo, [])
        if reserva in cola:
            cola.remove(reserva)
            reserva.cancelar()
            reserva.usuario.remover_reserva(reserva)
        if not cola:
            reserva.material.marcar_disponible()

    def siguiente_reserva(self, material: "Material") -> Optional[Reserva]:
        cola = self._reservas_por_material.get(material.codigo)
        if not cola:
            return None
        return cola[0]

    def notificar_disponibilidad(self, material: "Material") -> None:
        reserva = self.siguiente_reserva(material)
        if not reserva:
            material.marcar_disponible()
            return
        reserva.material.marcar_reservado()
        reserva.marcar_notificada()
        if self._notificacion_service:
            self._notificacion_service.notificar_material_disponible(reserva)

    def completar_reserva(self, reserva: Reserva) -> None:
        codigo = reserva.material.codigo
        cola = self._reservas_por_material.get(codigo, [])
        if reserva in cola:
            cola.remove(reserva)
            reserva.completar()
            reserva.usuario.remover_reserva(reserva)
        if not cola:
            reserva.material.marcar_disponible()

    def configurar_notificaciones(
        self, notificacion_service: Optional["NotificacionService"]
    ) -> None:
        if notificacion_service:
            self._notificacion_service = notificacion_service


__all__ = ["ReservaService"]
