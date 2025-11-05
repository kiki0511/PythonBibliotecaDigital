"""Excepción específica para materiales no disponibles."""

from typing import Optional

from .biblioteca_exception import BibliotecaException


class MaterialNoDisponibleException(BibliotecaException):
    """Se lanza cuando se intenta operar con un material no disponible."""

    def __init__(self, material_id: Optional[str] = None) -> None:
        mensaje = (
            f"Material no disponible para préstamo o reserva: {material_id}"
            if material_id
            else "Material no disponible para préstamo o reserva."
        )
        super().__init__(mensaje)


__all__ = ["MaterialNoDisponibleException"]
