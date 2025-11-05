"""Servicio para audiolibros."""

from __future__ import annotations

from biblioteca_digital.constantes import DIAS_PRESTAMO_AUDIOLIBRO

from .materiales_service import MaterialService


class AudiolibroService(MaterialService):
    """Aplica las políticas de préstamos a los audiolibros."""

    def __init__(self) -> None:
        super().__init__(dias_prestamo_base=DIAS_PRESTAMO_AUDIOLIBRO)


__all__ = ["AudiolibroService"]
