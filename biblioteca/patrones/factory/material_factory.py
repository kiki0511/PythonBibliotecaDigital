"""
Factory para crear materiales bibliográficos.
Implementa patrón Factory Method.
"""

from typing import Dict, Callable
from biblioteca_digital.entidades.materiales.material import Material


class MaterialFactory:
    """
    Factory para crear diferentes tipos de materiales.
    Implementa patrón Factory Method sin exponer clases concretas.
    """

    _contador_id = 0

    @staticmethod
    def crear_material(tipo: str, titulo: str, autor: str) -> Material:
        """
        Crea un material según el tipo especificado.

        Args:
            tipo: Tipo de material (Libro, Revista, eBook, Audiolibro)
            titulo: Título del material
            autor: Autor del material

        Returns:
            Instancia de Material (tipo base)

        Raises:
            ValueError: Si el tipo es desconocido
        """
        factories: Dict[str, Callable[[], Material]] = {
            "Libro": lambda: MaterialFactory._crear_libro(titulo, autor),
            "Revista": lambda: MaterialFactory._crear_revista(titulo, autor),
            "eBook": lambda: MaterialFactory._crear_ebook(titulo, autor),
            "Audiolibro": lambda: MaterialFactory._crear_audiolibro(titulo, autor)
        }

        if tipo not in factories:
            raise ValueError(f"Tipo de material desconocido: {tipo}")

        return factories[tipo]()

    @staticmethod
    def _generar_id() -> int:
        """Genera un ID único para materiales."""
        MaterialFactory._contador_id += 1
        return MaterialFactory._contador_id

    @staticmethod
    def _crear_libro(titulo: str, autor: str) -> 'Libro':
        """Crea un Libro con valores por defecto."""
        from biblioteca_digital.entidades.materiales.libro import Libro
        return Libro(
            id_material=MaterialFactory._generar_id(),
            titulo=titulo,
            autor=autor,
            isbn="978-3-16-148410-0",
            editorial="Editorial Ejemplo",
            num_paginas=350
        )

    @staticmethod
    def _crear_revista(titulo: str, autor: str) -> 'Revista':
        """Crea una Revista con valores por defecto."""
        from biblioteca_digital.entidades.materiales.revista import Revista
        return Revista(
            id_material=MaterialFactory._generar_id(),
            titulo=titulo,
            autor=autor,
            numero_edicion=42,
            periodicidad="Mensual"
        )

    @staticmethod
    def _crear_ebook(titulo: str, autor: str) -> 'eBook':
        """Crea un eBook con valores por defecto."""
        from biblioteca_digital.entidades.materiales.ebook import eBook
        return eBook(
            id_material=MaterialFactory._generar_id(),
            titulo=titulo,
            autor=autor,
            formato="PDF",
            tamanio_mb=5.2
        )

    @staticmethod
    def _crear_audiolibro(titulo: str, autor: str) -> 'Audiolibro':
        """Crea un Audiolibro con valores por defecto."""
        from biblioteca_digital.entidades.materiales.audiolibro import Audiolibro
        return Audiolibro(
            id_material=MaterialFactory._generar_id(),
            titulo=titulo,
            autor=autor,
            duracion_minutos=480,
            narrador="Narrador Profesional"
        )