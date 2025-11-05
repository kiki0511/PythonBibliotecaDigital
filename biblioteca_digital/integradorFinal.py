"""
INTEGRADOR FINAL - CONSOLIDACION COMPLETA DEL PROYECTO
============================================================================
Directorio raiz: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital
Fecha de generacion: 2025-11-05 09:05:45
Total de archivos integrados: 39
Total de directorios procesados: 17
============================================================================
"""

# ==============================================================================
# TABLA DE CONTENIDOS
# ==============================================================================

# DIRECTORIO: .
#   1. __init__.py
#   2. constantes.py
#   3. main.py
#
# DIRECTORIO: entidades
#   4. __init__.py
#
# DIRECTORIO: entidades/materiales
#   5. audiolibro.py
#   6. ebook.py
#   7. libro.py
#   8. material.py
#   9. revista.py
#
# DIRECTORIO: entidades/prestamos
#   10. prestamo.py
#   11. reserva.py
#
# DIRECTORIO: entidades/usuarios
#   12. membresia.py
#   13. usuario.py
#
# DIRECTORIO: excepciones
#   14. biblioteca_exception.py
#   15. material_no_disponible_exception.py
#   16. persistencia_exception.py
#   17. usuario_no_encontrado_exception.py
#
# DIRECTORIO: notificaciones
#   18. notificacion.py
#   19. notificacion_service.py
#
# DIRECTORIO: patrones
#   20. __init__.py
#
# DIRECTORIO: patrones/factory
#   21. material_factory.py
#
# DIRECTORIO: patrones/observer
#   22. observable.py
#   23. observer.py
#
# DIRECTORIO: patrones/singleton
#   24. singleton_meta.py
#
# DIRECTORIO: patrones/strategy
#   25. multa_strategy.py
#
# DIRECTORIO: patrones/strategy/impl
#   26. multa_estandar_strategy.py
#   27. multa_reducida_strategy.py
#   28. sin_multa_strategy.py
#
# DIRECTORIO: servicios
#   29. __init__.py
#
# DIRECTORIO: servicios/materiales
#   30. audiolibro_service.py
#   31. ebook_service.py
#   32. libro_service.py
#   33. material_service_registry.py
#   34. materiales_service.py
#   35. revista_service.py
#
# DIRECTORIO: servicios/prestamo
#   36. prestamo_service.py
#   37. reserva_service.py
#
# DIRECTORIO: servicios/usuarios
#   38. usuario_manager.py
#   39. usuario_service.py
#



################################################################################
# DIRECTORIO: .
################################################################################

# ==============================================================================
# ARCHIVO 1/39: __init__.py
# Directorio: .
# Ruta completa: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 2/39: constantes.py
# Directorio: .
# Ruta completa: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/constantes.py
# ==============================================================================

"""
Constantes del sistema de biblioteca digital.
Define valores fijos utilizados en toda la aplicación.
"""

# Días de préstamo por tipo de material
DIAS_PRESTAMO_LIBRO = 14
DIAS_PRESTAMO_REVISTA = 7
DIAS_PRESTAMO_EBOOK = 21
DIAS_PRESTAMO_AUDIOLIBRO = 10

# Multas por tipo de membresía (por día de retraso)
MULTA_BASICA_POR_DIA = 2.00
MULTA_ESTANDAR_POR_DIA = 1.00
MULTA_PREMIUM_POR_DIA = 0.00

# Días de anticipación para notificación de vencimiento
DIAS_NOTIFICACION_VENCIMIENTO = 3

# Tipos de membresía
TIPO_MEMBRESIA_BASICA = "Basica"
TIPO_MEMBRESIA_ESTANDAR = "Estandar"
TIPO_MEMBRESIA_PREMIUM = "Premium"

# Tipos de materiales
TIPO_MATERIAL_LIBRO = "Libro"
TIPO_MATERIAL_REVISTA = "Revista"
TIPO_MATERIAL_EBOOK = "eBook"
TIPO_MATERIAL_AUDIOLIBRO = "Audiolibro"

# Estados de préstamos
ESTADO_PRESTAMO_ACTIVO = "Activo"
ESTADO_PRESTAMO_DEVUELTO = "Devuelto"
ESTADO_PRESTAMO_VENCIDO = "Vencido"

# Estados de reservas
ESTADO_RESERVA_PENDIENTE = "Pendiente"
ESTADO_RESERVA_NOTIFICADA = "Notificada"
ESTADO_RESERVA_COMPLETADA = "Completada"
ESTADO_RESERVA_CANCELADA = "Cancelada"

# Estados de materiales
ESTADO_MATERIAL_DISPONIBLE = "Disponible"
ESTADO_MATERIAL_PRESTADO = "Prestado"
ESTADO_MATERIAL_RESERVADO = "Reservado"
ESTADO_MATERIAL_EN_MANTENIMIENTO = "En Mantenimiento"

# Persistencia
DIRECTORIO_DATA = "data"
EXTENSION_DATA = ".dat"

# Tipos de notificaciones
TIPO_NOTIF_PRESTAMO = "PRESTAMO"
TIPO_NOTIF_DEVOLUCION = "DEVOLUCION"
TIPO_NOTIF_RESERVA = "RESERVA"
TIPO_NOTIF_MULTA = "MULTA"
TIPO_NOTIF_VENCIMIENTO = "VENCIMIENTO"

# ==============================================================================
# ARCHIVO 3/39: main.py
# Directorio: .
# Ruta completa: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/main.py
# ==============================================================================

"""Ejecución demostrativa del sistema de biblioteca digital."""

from __future__ import annotations

from datetime import datetime, timedelta
from pathlib import Path

from biblioteca_digital.constantes import (
    MULTA_BASICA_POR_DIA,
    MULTA_ESTANDAR_POR_DIA,
    MULTA_PREMIUM_POR_DIA,
)
from biblioteca_digital.notificaciones.notificacion import Notificacion
from biblioteca_digital.notificaciones.notificacion_service import NotificacionService
from biblioteca_digital.patrones.factory.material_factory import MaterialFactory
from biblioteca_digital.patrones.observer.observer import Observer
from biblioteca_digital.servicios.materiales.material_service_registry import (
    MaterialServiceRegistry,
)
from biblioteca_digital.servicios.prestamo.prestamo_service import PrestamoService
from biblioteca_digital.servicios.prestamo.reserva_service import ReservaService
from biblioteca_digital.servicios.usuarios.usuario_manager import UsuarioManager
from biblioteca_digital.servicios.usuarios.usuario_service import UsuarioService


SEPARATOR = "=" * 70


class ConsoleNotifier(Observer[Notificacion]):
    """Observador que imprime las notificaciones con un formato uniforme."""

    def actualizar(self, evento: Notificacion) -> None:  # pragma: no cover - flujo interactivo
        print(f"  [NOTIFICACION] {evento.mensaje}")


def print_section(title: str) -> None:
    print(SEPARATOR)
    print(title.center(70))
    print(SEPARATOR)
    print()


def nombre_membresia_amigable(tipo: str) -> str:
    equivalencias = {"Basica": "Básico", "Estandar": "Estándar"}
    return equivalencias.get(tipo, tipo)


def formato_moneda(valor: float) -> str:
    return f"${valor:.2f}"


def ruta_relativa(path: Path) -> str:
    try:
        return path.relative_to(Path.cwd()).as_posix()
    except ValueError:
        return path.as_posix()


def main() -> None:
    print_section("SISTEMA DE GESTION DE BIBLIOTECA DIGITAL")

    # Servicios principales
    notificacion_service = NotificacionService()
    notificacion_service.agregar_observador(ConsoleNotifier())

    usuario_manager = UsuarioManager.get_instance()
    if hasattr(usuario_manager, "_usuarios"):
        usuario_manager._usuarios.clear()  # type: ignore[attr-defined]

    prestamo_service = PrestamoService(notificacion_service=notificacion_service)
    if hasattr(prestamo_service, "_prestamos"):
        prestamo_service._prestamos.clear()  # type: ignore[attr-defined]

    reserva_service = ReservaService.get_instance()
    reserva_service.configurar_notificaciones(notificacion_service)
    if hasattr(reserva_service, "_reservas_por_material"):
        reserva_service._reservas_por_material.clear()  # type: ignore[attr-defined]

    registry = MaterialServiceRegistry()

    # Singleton -----------------------------------------------------------------
    print_section("PATRON SINGLETON - UsuarioManager")
    print("[OK] Verificando Singleton...")
    manager1 = UsuarioManager.get_instance()
    manager2 = UsuarioManager.get_instance()
    print(f"manager1 ID: {id(manager1)}")
    print(f"manager2 ID: {id(manager2)}")
    print(f"Son la misma instancia: {manager1 is manager2}")
    print()

    # Registro de usuarios ------------------------------------------------------
    print_section("REGISTRAR USUARIOS CON DIFERENTES MEMBRESIAS")
    usuario_premium = usuario_manager.registrar_usuario(
        dni=12345678,
        nombre="Juan Perez",
        email="juan@email.com",
        tipo_membresia="Premium",
        persistir=False,
    )
    usuario_basico = usuario_manager.registrar_usuario(
        dni=87654321,
        nombre="Maria Lopez",
        email="maria@email.com",
        tipo_membresia="Basica",
        persistir=False,
    )
    usuario_estandar = usuario_manager.registrar_usuario(
        dni=11223344,
        nombre="Carlos Rodriguez",
        email="carlos@email.com",
        tipo_membresia="Estandar",
        persistir=False,
    )
    print(f"[OK] Usuario Premium registrado: {usuario_premium}")
    print(f"[OK] Usuario Básico registrado: {usuario_basico}")
    print(f"[OK] Usuario Estándar registrado: {usuario_estandar}")
    print()

    # Factory Method ------------------------------------------------------------
    print_section("PATRON FACTORY METHOD - Crear Materiales")
    libro = MaterialFactory.crear_material(
        tipo="Libro",
        titulo="Cien años de soledad",
        autor="Gabriel García Márquez",
        isbn="978-3-16-148410-0",
        editorial="Editorial Ejemplo",
        paginas=350,
    )
    revista = MaterialFactory.crear_material(
        tipo="Revista",
        titulo="National Geographic",
        autor="National Geographic Society",
        numero_edicion="42",
        periodicidad="Mensual",
    )
    ebook = MaterialFactory.crear_material(
        tipo="eBook",
        titulo="Python Programming",
        autor="Guido van Rossum",
        formato="PDF",
        tamano_mb=5.2,
    )
    audiolibro = MaterialFactory.crear_material(
        tipo="Audiolibro",
        titulo="El Principito",
        autor="Antoine de Saint-Exupéry",
        duracion_minutos=8 * 60,
        narrador="Narrador Profesional",
    )
    print(f"[OK] Libro creado: {libro}")
    print(f"[OK] Revista creada: {revista}")
    print(f"[OK] eBook creado: {ebook}")
    print(f"[OK] Audiolibro creado: {audiolibro}")
    print()

    # Registry -----------------------------------------------------------------
    print_section("PATRON REGISTRY - Dispatch Polimórfico")
    print("[OK] Obteniendo días de préstamo por tipo:")
    print(f"  Libro: {registry.obtener_dias_prestamo(libro)} días")
    print(f"  Revista: {registry.obtener_dias_prestamo(revista)} días")
    print(f"  eBook: {registry.obtener_dias_prestamo(ebook)} días")
    print(f"  Audiolibro: {registry.obtener_dias_prestamo(audiolibro)} días")
    print()
    print("[OK] Obteniendo descripciones específicas:")
    print(f"  {registry.obtener_descripcion(libro)}")
    print(f"  {registry.obtener_descripcion(revista)}")
    print(f"  {registry.obtener_descripcion(ebook)}")
    print(f"  {registry.obtener_descripcion(audiolibro)}")
    print()

    # Observer -----------------------------------------------------------------
    print_section("PATRON OBSERVER - Sistema de Notificaciones")
    print("[OK] Observador registrado en el sistema de notificaciones")
    print()

    # Préstamos ----------------------------------------------------------------
    print_section("REALIZAR PRESTAMOS")
    fecha_base = datetime(2025, 11, 3, 10, 0, 0)

    print("[ACCION] Usuario Premium solicita préstamo de libro...")
    prestamo_libro = prestamo_service.realizar_prestamo(
        usuario_premium, libro, fecha_prestamo=fecha_base
    )
    print(f"[OK] Préstamo #1: {prestamo_libro}")
    print(f"  Vence el: {prestamo_libro.fecha_vencimiento.date()}")
    print()

    print("[ACCION] Usuario Básico solicita préstamo de eBook...")
    prestamo_ebook = prestamo_service.realizar_prestamo(
        usuario_basico, ebook, fecha_prestamo=fecha_base
    )
    prestamo_ebook.fecha_vencimiento = fecha_base + timedelta(days=21)
    print(f"[OK] Préstamo #2: {prestamo_ebook}")
    print(f"  Vence el: {prestamo_ebook.fecha_vencimiento.date()}")
    print()

    # Strategy -----------------------------------------------------------------
    print_section("PATRON STRATEGY - Cálculo de Multas")
    print("[SIMULACION] Devoluciones con 5 días de retraso:")
    print()
    tarifas = {
        "Premium": MULTA_PREMIUM_POR_DIA,
        "Basica": MULTA_BASICA_POR_DIA,
        "Estandar": MULTA_ESTANDAR_POR_DIA,
    }
    for usuario in (usuario_premium, usuario_basico, usuario_estandar):
        etiqueta = nombre_membresia_amigable(usuario.membresia.tipo)
        multa = usuario.calcular_multa(5)
        estrategia = usuario.membresia.estrategia_multa.__class__.__name__
        print(f"Usuario {etiqueta} ({usuario.nombre}):")
        print("  Días de retraso: 5")
        print(f"  Multa: {formato_moneda(multa)}")
        print(
            f"  Estrategia: {estrategia} "
            f"({tarifas[usuario.membresia.tipo]:.2f}/día)"
        )
        print()

    # Devolución ---------------------------------------------------------------
    print_section("DEVOLVER MATERIALES Y CALCULAR MULTAS")
    print(f"[ACCION] Devolviendo: {libro.titulo}")
    fecha_devolucion = prestamo_libro.fecha_vencimiento
    multa_generada = prestamo_service.registrar_devolucion(
        prestamo_libro, fecha=fecha_devolucion
    )
    print(f"  Días de retraso: {prestamo_libro.calcular_dias_retraso()}")
    print(f"  Multa generada: {formato_moneda(multa_generada)}")
    print()

    # Reservas -----------------------------------------------------------------
    print_section("CREAR RESERVAS")
    print(f"[ACCION] Usuario Estándar intenta reservar: {revista.titulo}")
    reserva = reserva_service.crear_reserva(usuario_estandar, revista)
    print(
        f"[OK] Reserva #1: {revista.titulo} - {usuario_estandar.nombre} "
        f"[{reserva.estado}]"
    )
    reserva_service.notificar_disponibilidad(revista)
    print()

    # Persistencia -------------------------------------------------------------
    print_section("PERSISTENCIA - Guardar y Cargar Usuarios")
    usuario_service = UsuarioService()
    print("[ACCION] Guardando usuario en disco...")
    ruta_guardada = usuario_service.guardar_usuario(usuario_premium)
    ruta_rel = ruta_relativa(ruta_guardada)
    print(f"Usuario {usuario_premium.nombre} guardado en {ruta_rel}")
    print(f"[OK] Usuario guardado en: {ruta_rel}")
    print()
    print("[ACCION] Cargando usuario desde disco...")
    usuario_cargado = usuario_service.cargar_usuario(usuario_premium.nombre)
    print(f"Usuario {usuario_cargado.nombre} cargado desde {ruta_rel}")
    print(f"[OK] Usuario cargado: {usuario_cargado}")
    print(f"  DNI: {usuario_cargado.dni}")
    print(f"  Email: {usuario_cargado.email}")
    print(f"  Membresía: {usuario_cargado.membresia}")
    print()

    # Resumen ------------------------------------------------------------------
    print_section("RESUMEN DE PATRONES IMPLEMENTADOS")
    print("[OK] SINGLETON")
    print("  - UsuarioManager: Instancia única del gestor de usuarios")
    print("  - MaterialServiceRegistry: Instancia única del registro")
    print()
    print("[OK] FACTORY METHOD")
    print("  - MaterialFactory: Crea 4 tipos de materiales sin exponer clases")
    print("  - Tipos: Libro, Revista, eBook, Audiolibro")
    print()
    print("[OK] OBSERVER")
    print("  - NotificacionService: Observable[Notificacion]")
    print("  - ConsoleNotifier: Observer que imprime notificaciones")
    print("  - Notificaciones: Préstamo, Devolución, Reserva, Multa")
    print()
    print("[OK] STRATEGY")
    print("  - SinMultaStrategy: Membresía Premium (0.00/día)")
    print("  - MultaEstandarStrategy: Membresía Básica (2.00/día)")
    print("  - MultaReducidaStrategy: Membresía Estándar (1.00/día)")
    print()
    print("[OK] REGISTRY")
    print("  - MaterialServiceRegistry: Dispatch polimórfico")
    print("  - Operaciones: obtener_dias_prestamo(), obtener_descripcion()")
    print("  - Sin cascadas de isinstance()")
    print()

    print(SEPARATOR)
    print(
        "SISTEMA DE BIBLIOTECA DIGITAL - PRUEBA COMPLETADA EXITOSAMENTE".center(70)
    )
    print(SEPARATOR)


if __name__ == "__main__":  # pragma: no cover - punto de entrada manual
    main()



################################################################################
# DIRECTORIO: entidades
################################################################################

# ==============================================================================
# ARCHIVO 4/39: __init__.py
# Directorio: entidades
# Ruta completa: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/entidades/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: entidades/materiales
################################################################################

# ==============================================================================
# ARCHIVO 5/39: audiolibro.py
# Directorio: entidades/materiales
# Ruta completa: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/entidades/materiales/audiolibro.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 6/39: ebook.py
# Directorio: entidades/materiales
# Ruta completa: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/entidades/materiales/ebook.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 7/39: libro.py
# Directorio: entidades/materiales
# Ruta completa: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/entidades/materiales/libro.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 8/39: material.py
# Directorio: entidades/materiales
# Ruta completa: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/entidades/materiales/material.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 9/39: revista.py
# Directorio: entidades/materiales
# Ruta completa: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/entidades/materiales/revista.py
# ==============================================================================

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



################################################################################
# DIRECTORIO: entidades/prestamos
################################################################################

# ==============================================================================
# ARCHIVO 10/39: prestamo.py
# Directorio: entidades/prestamos
# Ruta completa: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/entidades/prestamos/prestamo.py
# ==============================================================================

"""Entidad que representa un préstamo de material."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, TYPE_CHECKING

from biblioteca_digital import constantes

if TYPE_CHECKING:
    from biblioteca_digital.entidades.materiales.material import Material
    from biblioteca_digital.entidades.usuarios.usuario import Usuario


@dataclass
class Prestamo:
    """Registra el préstamo de un material a un usuario."""

    usuario: "Usuario"
    material: "Material"
    fecha_prestamo: datetime
    fecha_vencimiento: datetime
    fecha_devolucion: Optional[datetime] = None
    estado: str = field(init=False, default=constantes.ESTADO_PRESTAMO_ACTIVO)

    def __post_init__(self) -> None:
        if self.fecha_vencimiento <= self.fecha_prestamo:
            raise ValueError("La fecha de vencimiento debe ser posterior al préstamo.")

    def marcar_vencido(self) -> None:
        if self.estado == constantes.ESTADO_PRESTAMO_ACTIVO:
            self.estado = constantes.ESTADO_PRESTAMO_VENCIDO

    def registrar_devolucion(self, fecha: Optional[datetime] = None) -> None:
        if self.estado == constantes.ESTADO_PRESTAMO_DEVUELTO:
            return
        self.fecha_devolucion = fecha or datetime.now()
        self.estado = constantes.ESTADO_PRESTAMO_DEVUELTO
        self.material.marcar_disponible()
        self.usuario.cerrar_prestamo(self)

    def calcular_dias_retraso(self, referencia: Optional[datetime] = None) -> int:
        referencia = referencia or self.fecha_devolucion or datetime.now()
        if referencia <= self.fecha_vencimiento:
            return 0
        delta = referencia.date() - self.fecha_vencimiento.date()
        return max(0, delta.days)

    def esta_activo(self) -> bool:
        return self.estado == constantes.ESTADO_PRESTAMO_ACTIVO

    def esta_vencido(self) -> bool:
        if self.estado == constantes.ESTADO_PRESTAMO_VENCIDO:
            return True
        if self.estado == constantes.ESTADO_PRESTAMO_ACTIVO:
            if datetime.now() > self.fecha_vencimiento:
                self.marcar_vencido()
                return True
        return False

    def __str__(self) -> str:
        return (
            f"{self.material.titulo} - {self.usuario.nombre} "
            f"(Vence: {self.fecha_vencimiento.date()})"
        )


__all__ = ["Prestamo"]


# ==============================================================================
# ARCHIVO 11/39: reserva.py
# Directorio: entidades/prestamos
# Ruta completa: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/entidades/prestamos/reserva.py
# ==============================================================================

"""Entidad Reserva."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, TYPE_CHECKING

from biblioteca_digital import constantes

if TYPE_CHECKING:
    from biblioteca_digital.entidades.materiales.material import Material
    from biblioteca_digital.entidades.usuarios.usuario import Usuario


@dataclass
class Reserva:
    """Reserva de un material actualmente no disponible."""

    usuario: "Usuario"
    material: "Material"
    fecha_reserva: datetime = field(default_factory=datetime.now)
    estado: str = field(default=constantes.ESTADO_RESERVA_PENDIENTE, init=False)
    fecha_notificacion: Optional[datetime] = None

    def marcar_notificada(self, fecha: Optional[datetime] = None) -> None:
        self.estado = constantes.ESTADO_RESERVA_NOTIFICADA
        self.fecha_notificacion = fecha or datetime.now()

    def completar(self) -> None:
        self.estado = constantes.ESTADO_RESERVA_COMPLETADA

    def cancelar(self) -> None:
        self.estado = constantes.ESTADO_RESERVA_CANCELADA

    def esta_pendiente(self) -> bool:
        return self.estado == constantes.ESTADO_RESERVA_PENDIENTE


__all__ = ["Reserva"]



################################################################################
# DIRECTORIO: entidades/usuarios
################################################################################

# ==============================================================================
# ARCHIVO 12/39: membresia.py
# Directorio: entidades/usuarios
# Ruta completa: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/entidades/usuarios/membresia.py
# ==============================================================================

"""Modelo de membresía de usuario."""

from __future__ import annotations

from dataclasses import dataclass

from biblioteca_digital import constantes
from biblioteca_digital.patrones.strategy.impl.multa_estandar_strategy import (
    MultaEstandarStrategy,
)
from biblioteca_digital.patrones.strategy.impl.multa_reducida_strategy import (
    MultaReducidaStrategy,
)
from biblioteca_digital.patrones.strategy.impl.sin_multa_strategy import SinMultaStrategy
from biblioteca_digital.patrones.strategy.multa_strategy import MultaStrategy

_ESTRATEGIAS: dict[str, MultaStrategy] = {
    constantes.TIPO_MEMBRESIA_BASICA: MultaEstandarStrategy(),
    constantes.TIPO_MEMBRESIA_ESTANDAR: MultaReducidaStrategy(),
    constantes.TIPO_MEMBRESIA_PREMIUM: SinMultaStrategy(),
}

_DIAS_PRESTAMO: dict[str, int] = {
    constantes.TIPO_MEMBRESIA_BASICA: 7,
    constantes.TIPO_MEMBRESIA_ESTANDAR: 14,
    constantes.TIPO_MEMBRESIA_PREMIUM: 30,
}


@dataclass(frozen=True)
class Membresia:
    """Representa una membresía con políticas de préstamo y multa."""

    tipo: str
    dias_prestamo: int
    estrategia_multa: MultaStrategy

    def calcular_multa(self, dias_retraso: int) -> float:
        return self.estrategia_multa.calcular_multa(dias_retraso)

    @classmethod
    def crear(cls, tipo: str) -> "Membresia":
        tipo_normalizado = tipo.capitalize()
        if tipo_normalizado not in _ESTRATEGIAS:
            raise ValueError(f"Tipo de membresía inválido: {tipo}")
        return cls(
            tipo=tipo_normalizado,
            dias_prestamo=_DIAS_PRESTAMO[tipo_normalizado],
            estrategia_multa=_ESTRATEGIAS[tipo_normalizado],
        )

    def __str__(self) -> str:
        return self.tipo


__all__ = ["Membresia"]


# ==============================================================================
# ARCHIVO 13/39: usuario.py
# Directorio: entidades/usuarios
# Ruta completa: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/entidades/usuarios/usuario.py
# ==============================================================================

"""Entidad que representa a los usuarios de la biblioteca."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import List, TYPE_CHECKING

from .membresia import Membresia

if TYPE_CHECKING:
    from biblioteca_digital.entidades.prestamos.prestamo import Prestamo
    from biblioteca_digital.entidades.prestamos.reserva import Reserva

_EMAIL_REGEX = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


@dataclass
class Usuario:
    """Modelo de dominio para usuarios registrados."""

    dni: int
    nombre: str
    email: str
    membresia: Membresia
    prestamos_activos: List["Prestamo"] = field(default_factory=list, init=False)
    reservas_activas: List["Reserva"] = field(default_factory=list, init=False)

    def __post_init__(self) -> None:
        if self.dni <= 0:
            raise ValueError("El DNI debe ser un entero positivo.")
        if not self.nombre:
            raise ValueError("El nombre no puede estar vacío.")
        if not _EMAIL_REGEX.match(self.email):
            raise ValueError(f"Email inválido: {self.email}")

    def calcular_multa(self, dias_retraso: int) -> float:
        return self.membresia.calcular_multa(dias_retraso)

    def registrar_prestamo(self, prestamo: "Prestamo") -> None:
        if prestamo not in self.prestamos_activos:
            self.prestamos_activos.append(prestamo)

    def cerrar_prestamo(self, prestamo: "Prestamo") -> None:
        if prestamo in self.prestamos_activos:
            self.prestamos_activos.remove(prestamo)

    def agregar_reserva(self, reserva: "Reserva") -> None:
        if reserva not in self.reservas_activas:
            self.reservas_activas.append(reserva)

    def remover_reserva(self, reserva: "Reserva") -> None:
        if reserva in self.reservas_activas:
            self.reservas_activas.remove(reserva)

    def __str__(self) -> str:
        return (
            f"Usuario: {self.nombre} (DNI: {self.dni}) - {self.membresia.tipo}"
        )


__all__ = ["Usuario"]



################################################################################
# DIRECTORIO: excepciones
################################################################################

# ==============================================================================
# ARCHIVO 14/39: biblioteca_exception.py
# Directorio: excepciones
# Ruta completa: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/excepciones/biblioteca_exception.py
# ==============================================================================

"""Excepciones base del dominio de la biblioteca digital."""


class BibliotecaException(Exception):
    """Excepción base para el dominio del sistema de biblioteca."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message


__all__ = ["BibliotecaException"]


# ==============================================================================
# ARCHIVO 15/39: material_no_disponible_exception.py
# Directorio: excepciones
# Ruta completa: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/excepciones/material_no_disponible_exception.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 16/39: persistencia_exception.py
# Directorio: excepciones
# Ruta completa: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/excepciones/persistencia_exception.py
# ==============================================================================

"""Excepción para errores de persistencia."""

from .biblioteca_exception import BibliotecaException


class PersistenciaException(BibliotecaException):
    """Se lanza ante errores de lectura o escritura en disco."""

    def __init__(self, message: str) -> None:
        super().__init__(f"Error de persistencia: {message}")


__all__ = ["PersistenciaException"]


# ==============================================================================
# ARCHIVO 17/39: usuario_no_encontrado_exception.py
# Directorio: excepciones
# Ruta completa: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/excepciones/usuario_no_encontrado_exception.py
# ==============================================================================

"""Excepción para operaciones con usuarios inexistentes."""

from typing import Optional

from .biblioteca_exception import BibliotecaException


class UsuarioNoEncontradoException(BibliotecaException):
    """Se lanza cuando no se encuentra un usuario en el sistema."""

    def __init__(self, dni: Optional[int] = None) -> None:
        mensaje = (
            f"Usuario con DNI {dni} no encontrado." if dni else "Usuario no encontrado."
        )
        super().__init__(mensaje)


__all__ = ["UsuarioNoEncontradoException"]



################################################################################
# DIRECTORIO: notificaciones
################################################################################

# ==============================================================================
# ARCHIVO 18/39: notificacion.py
# Directorio: notificaciones
# Ruta completa: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/notificaciones/notificacion.py
# ==============================================================================

"""Modelo de datos para notificaciones del sistema."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict


@dataclass(frozen=True)
class Notificacion:
    """Mensaje generado por el sistema ante un evento relevante."""

    tipo: str
    mensaje: str
    destinatario: str
    metadata: Dict[str, Any] = field(default_factory=dict)
    fecha: datetime = field(default_factory=datetime.now)


__all__ = ["Notificacion"]


# ==============================================================================
# ARCHIVO 19/39: notificacion_service.py
# Directorio: notificaciones
# Ruta completa: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/notificaciones/notificacion_service.py
# ==============================================================================

"""Servicio de notificaciones basado en el patrón Observer."""

from __future__ import annotations

from typing import Dict, Optional, TYPE_CHECKING

from biblioteca_digital import constantes
from biblioteca_digital.patrones.observer.observable import Observable

from .notificacion import Notificacion

if TYPE_CHECKING:
    from biblioteca_digital.entidades.materiales.material import Material
    from biblioteca_digital.entidades.prestamos.prestamo import Prestamo
    from biblioteca_digital.entidades.prestamos.reserva import Reserva
    from biblioteca_digital.entidades.usuarios.usuario import Usuario


class NotificacionService(Observable[Notificacion]):
    """Publica eventos relevantes del dominio a los observadores."""

    def emitir_notificacion(
        self,
        tipo: str,
        mensaje: str,
        destinatario: str,
        metadata: Optional[Dict[str, object]] = None,
    ) -> None:
        notificacion = Notificacion(
            tipo=tipo,
            mensaje=mensaje,
            destinatario=destinatario,
            metadata=metadata or {},
        )
        self.notificar(notificacion)

    def notificar_prestamo_registrado(self, prestamo: "Prestamo") -> None:
        mensaje = (
            f"Préstamo realizado: {prestamo.material.titulo} - "
            f"{prestamo.usuario.nombre}"
        )
        self.emitir_notificacion(
            constantes.TIPO_NOTIF_PRESTAMO,
            mensaje,
            destinatario=prestamo.usuario.email,
            metadata={"dni": prestamo.usuario.dni, "codigo_material": prestamo.material.codigo},
        )

    def notificar_devolucion_proxima(self, usuario: "Usuario", prestamo: "Prestamo") -> None:
        mensaje = (
            f"Recordatorio: el préstamo de '{prestamo.material.titulo}' "
            f"vence el {prestamo.fecha_vencimiento.date()}."
        )
        self.emitir_notificacion(
            constantes.TIPO_NOTIF_VENCIMIENTO,
            mensaje,
            destinatario=usuario.email,
            metadata={"codigo_material": prestamo.material.codigo},
        )

    def notificar_material_disponible(self, reserva: "Reserva") -> None:
        mensaje = (
            f"Material disponible: {reserva.material.titulo} "
            "está listo para préstamo"
        )
        self.emitir_notificacion(
            constantes.TIPO_NOTIF_RESERVA,
            mensaje,
            destinatario=reserva.usuario.email,
            metadata={"reserva": reserva.material.codigo},
        )

    def notificar_multa(self, usuario: "Usuario", monto: float, prestamo: "Prestamo") -> None:
        mensaje = (
            f"Se registró una multa de {monto:.2f} por el préstamo "
            f"de '{prestamo.material.titulo}'."
        )
        self.emitir_notificacion(
            constantes.TIPO_NOTIF_MULTA,
            mensaje,
            destinatario=usuario.email,
            metadata={"monto": monto, "dni": usuario.dni},
        )

    def notificar_prestamo_devuelto(self, prestamo: "Prestamo") -> None:
        mensaje = f"Material devuelto: {prestamo.material.titulo} - {prestamo.usuario.nombre}"
        self.emitir_notificacion(
            constantes.TIPO_NOTIF_DEVOLUCION,
            mensaje,
            destinatario=prestamo.usuario.email,
            metadata={"codigo_material": prestamo.material.codigo},
        )


__all__ = ["NotificacionService"]



################################################################################
# DIRECTORIO: patrones
################################################################################

# ==============================================================================
# ARCHIVO 20/39: __init__.py
# Directorio: patrones
# Ruta completa: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/patrones/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: patrones/factory
################################################################################

# ==============================================================================
# ARCHIVO 21/39: material_factory.py
# Directorio: patrones/factory
# Ruta completa: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/patrones/factory/material_factory.py
# ==============================================================================

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



################################################################################
# DIRECTORIO: patrones/observer
################################################################################

# ==============================================================================
# ARCHIVO 22/39: observable.py
# Directorio: patrones/observer
# Ruta completa: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/patrones/observer/observable.py
# ==============================================================================

"""Implementación base del patrón Observable."""

from __future__ import annotations

from typing import Generic, List, TypeVar

from .observer import Observer

T = TypeVar("T")


class Observable(Generic[T]):
    """Gestiona la suscripción de observadores y notificaciones."""

    def __init__(self) -> None:
        self._observadores: List[Observer[T]] = []

    def agregar_observador(self, observador: Observer[T]) -> None:
        if observador not in self._observadores:
            self._observadores.append(observador)

    def remover_observador(self, observador: Observer[T]) -> None:
        if observador in self._observadores:
            self._observadores.remove(observador)

    def notificar(self, evento: T) -> None:
        for observador in list(self._observadores):
            observador.actualizar(evento)


__all__ = ["Observable"]


# ==============================================================================
# ARCHIVO 23/39: observer.py
# Directorio: patrones/observer
# Ruta completa: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/patrones/observer/observer.py
# ==============================================================================

"""Interfaz del patrón Observer."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class Observer(ABC, Generic[T]):
    """Define la interfaz que deben implementar los observadores."""

    @abstractmethod
    def actualizar(self, evento: T) -> None:
        """Recibe una notificación con el evento emitido."""
        raise NotImplementedError


__all__ = ["Observer"]



################################################################################
# DIRECTORIO: patrones/singleton
################################################################################

# ==============================================================================
# ARCHIVO 24/39: singleton_meta.py
# Directorio: patrones/singleton
# Ruta completa: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/patrones/singleton/singleton_meta.py
# ==============================================================================

"""Metaclase para implementar el patrón Singleton thread-safe."""

from __future__ import annotations

from threading import RLock
from typing import Any, Dict, Type


class SingletonMeta(type):
    """Metaclase que garantiza una única instancia por clase."""

    _instances: Dict[Type, Any] = {}
    _lock: RLock = RLock()

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


__all__ = ["SingletonMeta"]



################################################################################
# DIRECTORIO: patrones/strategy
################################################################################

# ==============================================================================
# ARCHIVO 25/39: multa_strategy.py
# Directorio: patrones/strategy
# Ruta completa: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/patrones/strategy/multa_strategy.py
# ==============================================================================

"""Interfaz para las estrategias de cálculo de multas."""

from __future__ import annotations

from abc import ABC, abstractmethod


class MultaStrategy(ABC):
    """Define la operación para calcular multas por retraso."""

    @abstractmethod
    def calcular_multa(self, dias_retraso: int) -> float:
        """Devuelve el monto total de la multa para los días indicados."""
        raise NotImplementedError


__all__ = ["MultaStrategy"]



################################################################################
# DIRECTORIO: patrones/strategy/impl
################################################################################

# ==============================================================================
# ARCHIVO 26/39: multa_estandar_strategy.py
# Directorio: patrones/strategy/impl
# Ruta completa: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/patrones/strategy/impl/multa_estandar_strategy.py
# ==============================================================================

"""Estrategia de multa estándar para membresías básicas."""

from __future__ import annotations

from biblioteca_digital.constantes import MULTA_BASICA_POR_DIA

from ..multa_strategy import MultaStrategy


class MultaEstandarStrategy(MultaStrategy):
    """Aplica la multa fija por día configurada para membresía básica."""

    def calcular_multa(self, dias_retraso: int) -> float:
        return max(0, dias_retraso) * MULTA_BASICA_POR_DIA


__all__ = ["MultaEstandarStrategy"]


# ==============================================================================
# ARCHIVO 27/39: multa_reducida_strategy.py
# Directorio: patrones/strategy/impl
# Ruta completa: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/patrones/strategy/impl/multa_reducida_strategy.py
# ==============================================================================

"""Estrategia de multa reducida para membresías estándar."""

from __future__ import annotations

from biblioteca_digital.constantes import MULTA_ESTANDAR_POR_DIA

from ..multa_strategy import MultaStrategy


class MultaReducidaStrategy(MultaStrategy):
    """Aplica una multa menor para clientes con membresía estándar."""

    def calcular_multa(self, dias_retraso: int) -> float:
        return max(0, dias_retraso) * MULTA_ESTANDAR_POR_DIA


__all__ = ["MultaReducidaStrategy"]


# ==============================================================================
# ARCHIVO 28/39: sin_multa_strategy.py
# Directorio: patrones/strategy/impl
# Ruta completa: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/patrones/strategy/impl/sin_multa_strategy.py
# ==============================================================================

"""Estrategia que representa ausencia de multas."""

from __future__ import annotations

from ..multa_strategy import MultaStrategy


class SinMultaStrategy(MultaStrategy):
    """Devuelve cero independientemente del retraso."""

    def calcular_multa(self, dias_retraso: int) -> float:
        return 0.0


__all__ = ["SinMultaStrategy"]



################################################################################
# DIRECTORIO: servicios
################################################################################

# ==============================================================================
# ARCHIVO 29/39: __init__.py
# Directorio: servicios
# Ruta completa: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/servicios/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: servicios/materiales
################################################################################

# ==============================================================================
# ARCHIVO 30/39: audiolibro_service.py
# Directorio: servicios/materiales
# Ruta completa: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/servicios/materiales/audiolibro_service.py
# ==============================================================================

"""Servicio para audiolibros."""

from __future__ import annotations

from biblioteca_digital.constantes import DIAS_PRESTAMO_AUDIOLIBRO

from .materiales_service import MaterialService


class AudiolibroService(MaterialService):
    """Aplica las políticas de préstamos a los audiolibros."""

    def __init__(self) -> None:
        super().__init__(dias_prestamo_base=DIAS_PRESTAMO_AUDIOLIBRO)


__all__ = ["AudiolibroService"]


# ==============================================================================
# ARCHIVO 31/39: ebook_service.py
# Directorio: servicios/materiales
# Ruta completa: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/servicios/materiales/ebook_service.py
# ==============================================================================

"""Servicio específico para eBooks."""

from __future__ import annotations

from biblioteca_digital.constantes import DIAS_PRESTAMO_EBOOK

from .materiales_service import MaterialService


class EbookService(MaterialService):
    """Gestiona las reglas de préstamo para libros digitales."""

    def __init__(self) -> None:
        super().__init__(dias_prestamo_base=DIAS_PRESTAMO_EBOOK)


__all__ = ["EbookService"]


# ==============================================================================
# ARCHIVO 32/39: libro_service.py
# Directorio: servicios/materiales
# Ruta completa: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/servicios/materiales/libro_service.py
# ==============================================================================

"""Servicio específico para libros."""

from __future__ import annotations

from biblioteca_digital.constantes import DIAS_PRESTAMO_LIBRO

from .materiales_service import MaterialService


class LibroService(MaterialService):
    """Gestiona reglas de préstamo para libros físicos."""

    def __init__(self) -> None:
        super().__init__(dias_prestamo_base=DIAS_PRESTAMO_LIBRO)


__all__ = ["LibroService"]


# ==============================================================================
# ARCHIVO 33/39: material_service_registry.py
# Directorio: servicios/materiales
# Ruta completa: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/servicios/materiales/material_service_registry.py
# ==============================================================================

"""Registro centralizado de servicios de materiales."""

from __future__ import annotations

from typing import Dict, Iterable, Optional, TYPE_CHECKING, Union

from biblioteca_digital import constantes
from biblioteca_digital.entidades.materiales.material import Material
from biblioteca_digital.patrones.singleton.singleton_meta import SingletonMeta

from .audiolibro_service import AudiolibroService
from .ebook_service import EbookService
from .libro_service import LibroService
from .materiales_service import MaterialService
from .revista_service import RevistaService


if TYPE_CHECKING:
    from biblioteca_digital.entidades.usuarios.membresia import Membresia


class MaterialServiceRegistry(metaclass=SingletonMeta):
    """Patrón Registry + Singleton para acceder a servicios por tipo."""

    def __init__(self) -> None:
        self._servicios: Dict[str, MaterialService] = {
            constantes.TIPO_MATERIAL_LIBRO: LibroService(),
            constantes.TIPO_MATERIAL_REVISTA: RevistaService(),
            constantes.TIPO_MATERIAL_EBOOK: EbookService(),
            constantes.TIPO_MATERIAL_AUDIOLIBRO: AudiolibroService(),
        }

    def registrar_servicio(
        self, tipo_material: str, servicio: MaterialService
    ) -> None:
        self._servicios[tipo_material] = servicio

    def obtener_servicio(
        self, material_o_tipo: Union[Material, str]
    ) -> MaterialService:
        tipo = (
            material_o_tipo.tipo
            if isinstance(material_o_tipo, Material)
            else material_o_tipo
        )
        try:
            return self._servicios[tipo]
        except KeyError as exc:
            raise ValueError(f"No existe servicio registrado para {tipo}") from exc

    def obtener_dias_prestamo(
        self, material: Material, membresia: Optional["Membresia"] = None
    ) -> int:
        servicio = self.obtener_servicio(material)
        return servicio.calcular_dias_prestamo(membresia)

    def calcular_fecha_vencimiento(
        self,
        material: Material,
        membresia: Optional["Membresia"],
        fecha_referencia=None,
    ):
        servicio = self.obtener_servicio(material)
        return servicio.calcular_fecha_vencimiento(material, membresia, fecha_referencia)

    def tipos_registrados(self) -> Iterable[str]:
        return self._servicios.keys()

    def obtener_descripcion(self, material: Material) -> str:
        servicio = self.obtener_servicio(material)
        return servicio.descripcion(material)


__all__ = ["MaterialServiceRegistry"]


# ==============================================================================
# ARCHIVO 34/39: materiales_service.py
# Directorio: servicios/materiales
# Ruta completa: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/servicios/materiales/materiales_service.py
# ==============================================================================

"""Servicios base para operaciones sobre materiales."""

from __future__ import annotations

from abc import ABC
from datetime import datetime, timedelta
from typing import Optional, TYPE_CHECKING

from biblioteca_digital.excepciones.material_no_disponible_exception import (
    MaterialNoDisponibleException,
)

if TYPE_CHECKING:
    from biblioteca_digital.entidades.materiales.material import Material
    from biblioteca_digital.entidades.usuarios.membresia import Membresia


class MaterialService(ABC):
    """Servicio base reutilizable por los distintos tipos de materiales."""

    def __init__(self, dias_prestamo_base: int) -> None:
        self._dias_prestamo_base = dias_prestamo_base

    def validar_disponibilidad(self, material: "Material") -> None:
        if not material.esta_disponible():
            raise MaterialNoDisponibleException(material.codigo)

    def calcular_fecha_vencimiento(
        self,
        material: "Material",
        membresia: Optional["Membresia"],
        fecha_referencia: Optional[datetime] = None,
    ) -> datetime:
        dias = self.calcular_dias_prestamo(membresia)
        fecha_referencia = fecha_referencia or datetime.now()
        return fecha_referencia + timedelta(days=dias)

    def calcular_dias_prestamo(self, membresia: Optional["Membresia"]) -> int:
        if membresia:
            return min(self._dias_prestamo_base, membresia.dias_prestamo)
        return self._dias_prestamo_base

    def prestar(self, material: "Material") -> None:
        self.validar_disponibilidad(material)
        material.marcar_prestado()

    def devolver(self, material: "Material") -> None:
        material.marcar_disponible()

    def descripcion(self, material: "Material") -> str:
        return material.descripcion_detallada()


__all__ = ["MaterialService"]


# ==============================================================================
# ARCHIVO 35/39: revista_service.py
# Directorio: servicios/materiales
# Ruta completa: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/servicios/materiales/revista_service.py
# ==============================================================================

"""Servicio específico para revistas."""

from __future__ import annotations

from biblioteca_digital.constantes import DIAS_PRESTAMO_REVISTA

from .materiales_service import MaterialService


class RevistaService(MaterialService):
    """Gestiona el ciclo de vida de las revistas."""

    def __init__(self) -> None:
        super().__init__(dias_prestamo_base=DIAS_PRESTAMO_REVISTA)


__all__ = ["RevistaService"]



################################################################################
# DIRECTORIO: servicios/prestamo
################################################################################

# ==============================================================================
# ARCHIVO 36/39: prestamo_service.py
# Directorio: servicios/prestamo
# Ruta completa: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/servicios/prestamo/prestamo_service.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 37/39: reserva_service.py
# Directorio: servicios/prestamo
# Ruta completa: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/servicios/prestamo/reserva_service.py
# ==============================================================================

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



################################################################################
# DIRECTORIO: servicios/usuarios
################################################################################

# ==============================================================================
# ARCHIVO 38/39: usuario_manager.py
# Directorio: servicios/usuarios
# Ruta completa: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/servicios/usuarios/usuario_manager.py
# ==============================================================================

"""Gestor Singleton para usuarios del sistema."""

from __future__ import annotations

from typing import Dict, Iterable, Optional

from biblioteca_digital.entidades.usuarios.membresia import Membresia
from biblioteca_digital.entidades.usuarios.usuario import Usuario
from biblioteca_digital.excepciones.usuario_no_encontrado_exception import (
    UsuarioNoEncontradoException,
)
from biblioteca_digital.patrones.singleton.singleton_meta import SingletonMeta

from .usuario_service import UsuarioService


class UsuarioManager(metaclass=SingletonMeta):
    """Gestiona el ciclo de vida de los usuarios registrados."""

    def __init__(self, usuario_service: Optional[UsuarioService] = None) -> None:
        self._usuarios: Dict[int, Usuario] = {}
        self._usuario_service = usuario_service or UsuarioService()

    @classmethod
    def get_instance(cls) -> "UsuarioManager":
        return cls()

    def registrar_usuario(
        self, dni: int, nombre: str, email: str, tipo_membresia: str, persistir: bool = True
    ) -> Usuario:
        if dni in self._usuarios:
            raise ValueError(f"Usuario con DNI {dni} ya existe.")
        membresia = Membresia.crear(tipo_membresia)
        usuario = Usuario(dni=dni, nombre=nombre, email=email, membresia=membresia)
        self._usuarios[dni] = usuario
        if persistir:
            self._usuario_service.guardar_usuario(usuario)
        return usuario

    def buscar_usuario(self, dni: int) -> Usuario:
        try:
            return self._usuarios[dni]
        except KeyError as exc:
            raise UsuarioNoEncontradoException(dni) from exc

    def eliminar_usuario(self, dni: int) -> None:
        usuario = self.buscar_usuario(dni)
        if usuario.prestamos_activos:
            raise ValueError("No se puede eliminar usuario con préstamos activos.")
        self._usuarios.pop(dni, None)

    def listar_usuarios(self) -> Iterable[Usuario]:
        return self._usuarios.values()

    def cargar_desde_disco(self, nombre_archivo: str) -> Usuario:
        usuario = self._usuario_service.cargar_usuario(nombre_archivo)
        self._usuarios[usuario.dni] = usuario
        return usuario


__all__ = ["UsuarioManager"]


# ==============================================================================
# ARCHIVO 39/39: usuario_service.py
# Directorio: servicios/usuarios
# Ruta completa: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/servicios/usuarios/usuario_service.py
# ==============================================================================

"""Servicio para la persistencia de usuarios en disco."""

from __future__ import annotations

import pickle
from pathlib import Path
from typing import Optional

from biblioteca_digital import constantes
from biblioteca_digital.entidades.usuarios.usuario import Usuario
from biblioteca_digital.excepciones.persistencia_exception import PersistenciaException


class UsuarioService:
    """Gestiona la serialización y deserialización de usuarios."""

    def __init__(self, base_path: Optional[Path] = None) -> None:
        raiz_proyecto = Path(__file__).resolve().parents[3]
        self._data_dir = (base_path or raiz_proyecto / constantes.DIRECTORIO_DATA)
        self._data_dir.mkdir(exist_ok=True)

    def _obtener_ruta(self, identificador: str) -> Path:
        nombre = identificador.strip()
        if not nombre:
            raise PersistenciaException("Nombre de archivo vacío.")
        return self._data_dir / f"{nombre}{constantes.EXTENSION_DATA}"

    def guardar_usuario(self, usuario: Usuario, identificador: Optional[str] = None) -> Path:
        ruta = self._obtener_ruta(identificador or usuario.nombre)
        try:
            with ruta.open("wb") as archivo:
                pickle.dump(usuario, archivo)
        except OSError as exc:
            raise PersistenciaException(str(exc)) from exc
        return ruta

    def cargar_usuario(self, identificador: str) -> Usuario:
        ruta = self._obtener_ruta(identificador)
        try:
            with ruta.open("rb") as archivo:
                usuario: Usuario = pickle.load(archivo)
        except FileNotFoundError as exc:
            raise PersistenciaException(f"No existe archivo {ruta.name}") from exc
        except OSError as exc:
            raise PersistenciaException(str(exc)) from exc
        return usuario



################################################################################
# FIN DEL INTEGRADOR FINAL
# Total de archivos: 39
# Generado: 2025-11-05 09:05:45
################################################################################
