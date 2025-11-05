"""
Archivo integrador generado automaticamente
Directorio: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/servicios/prestamo
Fecha: 2025-11-05 09:05:45
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: prestamo_service.py
# Ruta: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/servicios/prestamo/prestamo_service.py
# ================================================================================

"""Servicio de dominio para gestionar préstamos."""

from __future__ import annotations

from datetime import datetime, timedelta
from typing import List, Optional, TYPE_CHECKING

from biblioteca_digital import constantes
from biblioteca_digital.entidades.prestamos.prestamo import Prestamo
from biblioteca_digital.patrones.singleton.singleton_meta import SingletonMeta
from biblioteca_digital.servicios.materiales.material_service_registry import (
    MaterialServiceRegistry,
)
from biblioteca_digital.servicios.prestamo.reserva_service import ReservaService

if TYPE_CHECKING:
    from biblioteca_digital.entidades.materiales.material import Material
    from biblioteca_digital.entidades.usuarios.usuario import Usuario
    from biblioteca_digital.notificaciones.notificacion_service import NotificacionService


class PrestamoService(metaclass=SingletonMeta):
    """Gestiona la operatoria de préstamos y devoluciones."""

    def __init__(
        self,
        notificacion_service: Optional["NotificacionService"] = None,
        reserva_service: Optional[ReservaService] = None,
    ) -> None:
        self._material_registry = MaterialServiceRegistry()
        self._notificacion_service = notificacion_service
        self._reserva_service = reserva_service or ReservaService()
        self._reserva_service.configurar_notificaciones(notificacion_service)
        self._prestamos: List[Prestamo] = []

    @classmethod
    def get_instance(cls) -> "PrestamoService":
        return cls()

    def realizar_prestamo(
        self,
        usuario: "Usuario",
        material: "Material",
        fecha_prestamo: Optional[datetime] = None,
    ) -> Prestamo:
        servicio_material = self._material_registry.obtener_servicio(material)
        servicio_material.prestar(material)
        fecha_prestamo = fecha_prestamo or datetime.now()
        fecha_vencimiento = self._material_registry.calcular_fecha_vencimiento(
            material, usuario.membresia, fecha_referencia=fecha_prestamo
        )
        prestamo = Prestamo(
            usuario=usuario,
            material=material,
            fecha_prestamo=fecha_prestamo,
            fecha_vencimiento=fecha_vencimiento,
        )
        usuario.registrar_prestamo(prestamo)
        self._prestamos.append(prestamo)
        if self._notificacion_service:
            self._notificacion_service.notificar_prestamo_registrado(prestamo)
        return prestamo

    def registrar_devolucion(
        self, prestamo: Prestamo, fecha: Optional[datetime] = None
    ) -> float:
        prestamo.registrar_devolucion(fecha)
        multa = 0.0
        dias_retraso = prestamo.calcular_dias_retraso()
        if dias_retraso > 0:
            multa = prestamo.usuario.calcular_multa(dias_retraso)
            if self._notificacion_service and multa > 0:
                self._notificacion_service.notificar_multa(
                    prestamo.usuario, multa, prestamo
                )
        if self._notificacion_service:
            self._notificacion_service.notificar_prestamo_devuelto(prestamo)
        if self._reserva_service:
            self._reserva_service.notificar_disponibilidad(prestamo.material)
        return multa

    def prestamos_activos(self) -> List[Prestamo]:
        return [prestamo for prestamo in self._prestamos if prestamo.esta_activo()]

    def prestamos_por_usuario(self, usuario: "Usuario") -> List[Prestamo]:
        return [p for p in self._prestamos if p.usuario == usuario and p.esta_activo()]

    def verificar_vencimientos(self) -> None:
        if not self._notificacion_service:
            return
        limite_notificacion = timedelta(days=constantes.DIAS_NOTIFICACION_VENCIMIENTO)
        ahora = datetime.now()
        for prestamo in self.prestamos_activos():
            faltante = prestamo.fecha_vencimiento - ahora
            if timedelta(0) <= faltante <= limite_notificacion:
                self._notificacion_service.notificar_devolucion_proxima(
                    prestamo.usuario, prestamo
                )


__all__ = ["PrestamoService"]


# ================================================================================
# ARCHIVO 2/2: reserva_service.py
# Ruta: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/servicios/prestamo/reserva_service.py
# ================================================================================

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


