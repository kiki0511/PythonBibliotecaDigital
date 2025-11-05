"""Servicio específico para eBooks."""

from __future__ import annotations

from biblioteca_digital.constantes import DIAS_PRESTAMO_EBOOK

from .materiales_service import MaterialService


class EbookService(MaterialService):
    """Gestiona las reglas de préstamo para libros digitales."""

    def __init__(self) -> None:
        super().__init__(dias_prestamo_base=DIAS_PRESTAMO_EBOOK)


__all__ = ["EbookService"]
