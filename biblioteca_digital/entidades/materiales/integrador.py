"""
Archivo integrador generado automaticamente
Directorio: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/entidades/materiales
Fecha: 2025-11-05 09:05:45
Total de archivos integrados: 5
"""

# ================================================================================
# ARCHIVO 1/5: audiolibro.py
# Ruta: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/entidades/materiales/audiolibro.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 2/5: ebook.py
# Ruta: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/entidades/materiales/ebook.py
# ================================================================================

"""Entidad eBook."""

from __future__ import annotations

from typing import Optional

from biblioteca_digital import constantes

from .material import Material


class Ebook(Material):
    """Libro digital con metadatos de formato."""

    TIPO: str = constantes.TIPO_MATERIAL_EBOOK

    def __init__(
        self,
        titulo: str,
        autor: str,
        formato: str,
        tamano_mb: float,
        codigo: Optional[str] = None,
    ) -> None:
        super().__init__(titulo=titulo, autor=autor, codigo=codigo)
        self.formato = formato
        self.tamano_mb = tamano_mb

    def __str__(self) -> str:
        return f"eBook: {self.titulo} - {self.autor} ({self.formato}, {self.tamano_mb:.1f}MB)"

    def descripcion_detallada(self) -> str:
        return f"eBook formato {self.formato}, {self.tamano_mb:.1f}MB"


__all__ = ["Ebook"]


# ================================================================================
# ARCHIVO 3/5: libro.py
# Ruta: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/entidades/materiales/libro.py
# ================================================================================

"""Entidad Libro que extiende Material."""

from __future__ import annotations

from typing import Optional

from biblioteca_digital import constantes

from .material import Material


class Libro(Material):
    """Representa un libro físico tradicional."""

    TIPO: str = constantes.TIPO_MATERIAL_LIBRO

    def __init__(
        self,
        titulo: str,
        autor: str,
        isbn: str,
        editorial: Optional[str] = None,
        paginas: Optional[int] = None,
        codigo: Optional[str] = None,
    ) -> None:
        super().__init__(titulo=titulo, autor=autor, codigo=codigo)
        self.isbn = isbn
        self.editorial = editorial
        self.paginas = paginas

    def __str__(self) -> str:
        detalles = [f"ISBN: {self.isbn}"]
        if self.paginas is not None:
            detalles.append(f"{self.paginas} páginas")
        if self.editorial:
            detalles.append(f"Editorial: {self.editorial}")
        det_str = ", ".join(detalles)
        return f"Libro: {self.titulo} - {self.autor} ({det_str})"

    def descripcion_detallada(self) -> str:
        partes = [f"Libro ISBN: {self.isbn}"]
        if self.paginas is not None:
            partes.append(f"{self.paginas} páginas")
        if self.editorial:
            partes.append(f"Editorial: {self.editorial}")
        return ", ".join(partes)


__all__ = ["Libro"]


# ================================================================================
# ARCHIVO 4/5: material.py
# Ruta: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/entidades/materiales/material.py
# ================================================================================

"""Modelos de materiales disponibles en la biblioteca."""

from __future__ import annotations

from typing import Optional

from biblioteca_digital import constantes


class Material:
    """Modelo base para cualquier material bibliográfico."""

    TIPO: str = "Material"

    def __init__(self, titulo: str, autor: str, codigo: Optional[str] = None) -> None:
        self.titulo = titulo
        self.autor = autor
        slug = self.titulo.lower().replace(" ", "-")
        self.codigo = codigo or f"{self.TIPO.lower()}-{slug}"
        self.estado = constantes.ESTADO_MATERIAL_DISPONIBLE

    @property
    def tipo(self) -> str:
        return self.TIPO

    def esta_disponible(self) -> bool:
        return self.estado == constantes.ESTADO_MATERIAL_DISPONIBLE

    def marcar_prestado(self) -> None:
        self.estado = constantes.ESTADO_MATERIAL_PRESTADO

    def marcar_disponible(self) -> None:
        self.estado = constantes.ESTADO_MATERIAL_DISPONIBLE

    def marcar_reservado(self) -> None:
        self.estado = constantes.ESTADO_MATERIAL_RESERVADO

    def marcar_en_mantenimiento(self) -> None:
        self.estado = constantes.ESTADO_MATERIAL_EN_MANTENIMIENTO

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(titulo='{self.titulo}', autor='{self.autor}')"

    def __str__(self) -> str:
        return f"{self.tipo}: {self.titulo} - {self.autor}"

    def descripcion_detallada(self) -> str:
        return str(self)


__all__ = ["Material"]


# ================================================================================
# ARCHIVO 5/5: revista.py
# Ruta: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/entidades/materiales/revista.py
# ================================================================================

"""Entidad Revista."""

from __future__ import annotations

from typing import Optional

from biblioteca_digital import constantes

from .material import Material


class Revista(Material):
    """Revista periódica disponible en la biblioteca."""

    TIPO: str = constantes.TIPO_MATERIAL_REVISTA

    def __init__(
        self,
        titulo: str,
        autor: str,
        numero_edicion: str,
        periodicidad: str,
        codigo: Optional[str] = None,
    ) -> None:
        super().__init__(titulo=titulo, autor=autor, codigo=codigo)
        self.numero_edicion = numero_edicion
        self.periodicidad = periodicidad

    def __str__(self) -> str:
        return f"Revista: {self.titulo} #{self.numero_edicion} - {self.periodicidad}"

    def descripcion_detallada(self) -> str:
        return f"Revista #{self.numero_edicion}, Periodicidad: {self.periodicidad}"


__all__ = ["Revista"]


