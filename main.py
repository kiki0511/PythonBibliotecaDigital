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
