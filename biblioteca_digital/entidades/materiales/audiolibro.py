"""Entidad Audiolibro."""

from __future__ import annotations

from typing import Optional

from biblioteca_digital import constantes

from .material import Material


class Audiolibro(Material):
    """Libro narrado en formato de audio."""

    TIPO: str = constantes.TIPO_MATERIAL_AUDIOLIBRO

    def __init__(
        self,
        titulo: str,
        autor: str,
        duracion_minutos: int,
        narrador: str,
        codigo: Optional[str] = None,
    ) -> None:
        super().__init__(titulo=titulo, autor=autor, codigo=codigo)
        self.duracion_minutos = duracion_minutos
        self.narrador = narrador

    def __str__(self) -> str:
        horas, minutos = divmod(self.duracion_minutos, 60)
        return (
            f"Audiolibro: {self.titulo} - {self.autor} "
            f"({horas}h {minutos}min, narrado por {self.narrador})"
        )

    def descripcion_detallada(self) -> str:
        horas, minutos = divmod(self.duracion_minutos, 60)
        return f"Audiolibro {horas}h {minutos}min, narrado por {self.narrador}"


__all__ = ["Audiolibro"]
