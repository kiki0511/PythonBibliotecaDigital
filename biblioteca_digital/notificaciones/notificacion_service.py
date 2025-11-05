"""Servicio de notificaciones basado en el patrón Observer."""

from __future__ import annotations

from typing import Dict, Optional, TYPE_CHECKING

from biblioteca_digital import constantes
from biblioteca_digital.patrones.observer.observable import Observable

from .notificacion import Notificacion

if TYPE_CHECKING:
    from biblioteca_digital.entidades.materiales.material import Material
    from biblioteca_digital.entidades.prestamos.prestamo import Prestamo
    from biblioteca_digital.entidades.prestamos.reserva import Reserva
    from biblioteca_digital.entidades.usuarios.usuario import Usuario


class NotificacionService(Observable[Notificacion]):
    """Publica eventos relevantes del dominio a los observadores."""

    def emitir_notificacion(
        self,
        tipo: str,
        mensaje: str,
        destinatario: str,
        metadata: Optional[Dict[str, object]] = None,
    ) -> None:
        notificacion = Notificacion(
            tipo=tipo,
            mensaje=mensaje,
            destinatario=destinatario,
            metadata=metadata or {},
        )
        self.notificar(notificacion)

    def notificar_prestamo_registrado(self, prestamo: "Prestamo") -> None:
        mensaje = (
            f"Préstamo realizado: {prestamo.material.titulo} - "
            f"{prestamo.usuario.nombre}"
        )
        self.emitir_notificacion(
            constantes.TIPO_NOTIF_PRESTAMO,
            mensaje,
            destinatario=prestamo.usuario.email,
            metadata={"dni": prestamo.usuario.dni, "codigo_material": prestamo.material.codigo},
        )

    def notificar_devolucion_proxima(self, usuario: "Usuario", prestamo: "Prestamo") -> None:
        mensaje = (
            f"Recordatorio: el préstamo de '{prestamo.material.titulo}' "
            f"vence el {prestamo.fecha_vencimiento.date()}."
        )
        self.emitir_notificacion(
            constantes.TIPO_NOTIF_VENCIMIENTO,
            mensaje,
            destinatario=usuario.email,
            metadata={"codigo_material": prestamo.material.codigo},
        )

    def notificar_material_disponible(self, reserva: "Reserva") -> None:
        mensaje = (
            f"Material disponible: {reserva.material.titulo} "
            "está listo para préstamo"
        )
        self.emitir_notificacion(
            constantes.TIPO_NOTIF_RESERVA,
            mensaje,
            destinatario=reserva.usuario.email,
            metadata={"reserva": reserva.material.codigo},
        )

    def notificar_multa(self, usuario: "Usuario", monto: float, prestamo: "Prestamo") -> None:
        mensaje = (
            f"Se registró una multa de {monto:.2f} por el préstamo "
            f"de '{prestamo.material.titulo}'."
        )
        self.emitir_notificacion(
            constantes.TIPO_NOTIF_MULTA,
            mensaje,
            destinatario=usuario.email,
            metadata={"monto": monto, "dni": usuario.dni},
        )

    def notificar_prestamo_devuelto(self, prestamo: "Prestamo") -> None:
        mensaje = f"Material devuelto: {prestamo.material.titulo} - {prestamo.usuario.nombre}"
        self.emitir_notificacion(
            constantes.TIPO_NOTIF_DEVOLUCION,
            mensaje,
            destinatario=prestamo.usuario.email,
            metadata={"codigo_material": prestamo.material.codigo},
        )


__all__ = ["NotificacionService"]
