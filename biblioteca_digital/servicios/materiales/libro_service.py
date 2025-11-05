"""Servicio específico para libros."""

from __future__ import annotations

from biblioteca_digital.constantes import DIAS_PRESTAMO_LIBRO

from .materiales_service import MaterialService


class LibroService(MaterialService):
    """Gestiona reglas de préstamo para libros físicos."""

    def __init__(self) -> None:
        super().__init__(dias_prestamo_base=DIAS_PRESTAMO_LIBRO)


__all__ = ["LibroService"]
