"""
Archivo integrador generado automaticamente
Directorio: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/patrones/factory
Fecha: 2025-11-05 09:05:45
Total de archivos integrados: 1
"""

# ================================================================================
# ARCHIVO 1/1: material_factory.py
# Ruta: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/patrones/factory/material_factory.py
# ================================================================================

"""Factory Method para la creación de materiales."""

from __future__ import annotations

from typing import Any, Dict, Type

from biblioteca_digital import constantes
from biblioteca_digital.entidades.materiales.audiolibro import Audiolibro
from biblioteca_digital.entidades.materiales.ebook import Ebook
from biblioteca_digital.entidades.materiales.libro import Libro
from biblioteca_digital.entidades.materiales.material import Material
from biblioteca_digital.entidades.materiales.revista import Revista


class MaterialFactory:
    """Encapsula la lógica de instanciación de materiales."""

    _mapa_constructores: Dict[str, Type[Material]] = {
        constantes.TIPO_MATERIAL_LIBRO.lower(): Libro,
        constantes.TIPO_MATERIAL_REVISTA.lower(): Revista,
        constantes.TIPO_MATERIAL_EBOOK.lower(): Ebook,
        constantes.TIPO_MATERIAL_AUDIOLIBRO.lower(): Audiolibro,
    }

    @classmethod
    def crear_material(cls, tipo: str, **datos: Any) -> Material:
        clave = tipo.strip().lower()
        try:
            constructor = cls._mapa_constructores[clave]
        except KeyError as exc:
            raise ValueError(f"Tipo de material no soportado: {tipo}") from exc
        return constructor(**datos)


__all__ = ["MaterialFactory"]


