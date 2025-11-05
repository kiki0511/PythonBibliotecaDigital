"""
Servicio de notificaciones del sistema.
Implementa patrón Observer.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from biblioteca_digital.entidades.usuarios.usuario import Usuario
    from biblioteca_digital.entidades.materiales.material import Material
    from biblioteca_digital.entidades.prestamos.prestamo import Prestamo

from biblioteca_digital.patrones.observer.observable import Observable
from biblioteca_digital.notificaciones.notificacion import Notificacion
from biblioteca_digital.constantes import (
    TIPO_NOTIF_PRESTAMO,
    TIPO_NOTIF_DEVOLUCION,
    TIPO_NOTIF_RESERVA,
    TIPO_NOTIF_MULTA,
    TIPO_NOTIF_VENCIMIENTO
)


class NotificacionService(Observable[Notificacion]):
    """
    Servicio de notificaciones del sistema.
    Implementa Observable[Notificacion] para el patrón Observer.
    """

    def __init__(self):
        """Inicializa el servicio de notificaciones."""
        super().__init__()

    def notificar_prestamo_realizado(
        self,
        usuario: 'Usuario',
        material: 'Material'
    ) -> None:
        """
        Notifica que se realizó un préstamo.

        Args:
            usuario: Usuario que realizó el préstamo
            material: Material prestado
        """
        mensaje = f"Préstamo realizado: {material.get_titulo()} - {usuario.get_nombre()}"
        notificacion = Notificacion(TIPO_NOTIF_PRESTAMO, mensaje, usuario)
        self.notificar_observadores(notificacion)

    def notificar_devolucion(
        self,
        usuario: 'Usuario',
        material: 'Material'
    ) -> None:
        """
        Notifica que se devolvió un material.

        Args:
            usuario: Usuario que devolvió
            material: Material devuelto
        """
        mensaje = f"Material devuelto: {material.get_titulo()} - {usuario.get_nombre()}"
        notificacion = Notificacion(TIPO_NOTIF_DEVOLUCION, mensaje, usuario)
        self.notificar_observadores(notificacion)

    def notificar_material_disponible(
        self,
        usuario: 'Usuario',
        material: 'Material'
    ) -> None:
        """
        Notifica que un material reservado está disponible.

        Args:
            usuario: Usuario que había reservado
            material: Material ahora disponible
        """
        mensaje = f"Material disponible: {material.get_titulo()} está listo para préstamo"
        notificacion = Notificacion(TIPO_NOTIF_RESERVA, mensaje, usuario)
        self.notificar_observadores(notificacion)

    def notificar_devolucion_proxima(
        self,
        usuario: 'Usuario',
        prestamo: 'Prestamo'
    ) -> None:
        """
        Notifica que un préstamo está próximo a vencer.

        Args:
            usuario: Usuario con préstamo próximo a vencer
            prestamo: Préstamo que vence pronto
        """
        mensaje = f"Recordatorio: {prestamo.get_material().get_titulo()} vence el {prestamo.get_fecha_vencimiento()}"
        notificacion = Notificacion(TIPO_NOTIF_VENCIMIENTO, mensaje, usuario)
        self.notificar_observadores(notificacion)

    def notificar_multa(
        self,
        usuario: 'Usuario',
        multa: float,
        dias_retraso: int
    ) -> None:
        """
        Notifica que se generó una multa.

        Args:
            usuario: Usuario con multa
            multa: Monto de la multa
            dias_retraso: Días de retraso
        """
        mensaje = f"Multa generada: ${multa:.2f} por {dias_retraso} días de retraso - {usuario.get_nombre()}"
        notificacion = Notificacion(TIPO_NOTIF_MULTA, mensaje, usuario)
        self.notificar_observadores(notificacion)