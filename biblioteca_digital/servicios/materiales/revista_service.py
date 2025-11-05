"""Servicio específico para revistas."""

from __future__ import annotations

from biblioteca_digital.constantes import DIAS_PRESTAMO_REVISTA

from .materiales_service import MaterialService


class RevistaService(MaterialService):
    """Gestiona el ciclo de vida de las revistas."""

    def __init__(self) -> None:
        super().__init__(dias_prestamo_base=DIAS_PRESTAMO_REVISTA)


__all__ = ["RevistaService"]
