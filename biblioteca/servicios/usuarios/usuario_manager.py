"""
Gestor de usuarios del sistema.
Implementa patrón Singleton para garantizar instancia única.
"""

from threading import Lock
from typing import Dict, Optional
from biblioteca_digital.entidades.usuarios.usuario import Usuario
from biblioteca_digital.entidades.usuarios.membresia import Membresia
from biblioteca_digital.patrones.strategy.impl.sin_multa_strategy import SinMultaStrategy
from biblioteca_digital.patrones.strategy.impl.multa_estandar_strategy import MultaEstandarStrategy
from biblioteca_digital.patrones.strategy.impl.multa_reducida_strategy import MultaReducidaStrategy
from biblioteca_digital.excepciones.biblioteca_exception import BibliotecaException
from biblioteca_digital.constantes import (
    TIPO_MEMBRESIA_BASICA,
    TIPO_MEMBRESIA_ESTANDAR,
    TIPO_MEMBRESIA_PREMIUM
)


class UsuarioManager:
    """
    Gestor único de usuarios del sistema.
    Implementa patrón Singleton para garantizar instancia única.
    Thread-safe con double-checked locking.
    """

    _instance: Optional['UsuarioManager'] = None
    _lock: Lock = Lock()

    def __new__(cls):
        """
        Controla la creación de instancias (Singleton).

        Returns:
            Instancia única de UsuarioManager
        """
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._inicializado = False
        return cls._instance

    def __init__(self):
        """Inicializa el gestor (solo una vez)."""
        if not self._inicializado:
            self._usuarios: Dict[int, Usuario] = {}
            self._membresias = self._crear_membresias()
            self._inicializado = True

    def _crear_membresias(self) -> Dict[str, Membresia]:
        """
        Crea los tipos de membresías disponibles.

        Returns:
            Diccionario de membresías por tipo
        """
        return {
            TIPO_MEMBRESIA_BASICA: Membresia(
                tipo=TIPO_MEMBRESIA_BASICA,
                dias_prestamo=7,
                descripcion="Membresía básica - 7 días de préstamo"
            ),
            TIPO_MEMBRESIA_ESTANDAR: Membresia(
                tipo=TIPO_MEMBRESIA_ESTANDAR,
                dias_prestamo=14,
                descripcion="Membresía estándar - 14 días de préstamo"
            ),
            TIPO_MEMBRESIA_PREMIUM: Membresia(
                tipo=TIPO_MEMBRESIA_PREMIUM,
                dias_prestamo=30,
                descripcion="Membresía premium - 30 días de préstamo, sin multas"
            )
        }

    @classmethod
    def get_instance(cls) -> 'UsuarioManager':
        """
        Obtiene la instancia única del gestor.

        Returns:
            Instancia única de UsuarioManager
        """
        if cls._instance is None:
            cls()
        return cls._instance

    def registrar_usuario(
        self,
        dni: int,
        nombre: str,
        email: str,
        tipo_membresia: str
    ) -> Usuario:
        """
        Registra un nuevo usuario en el sistema.

        Args:
            dni: DNI único del usuario
            nombre: Nombre completo
            email: Email de contacto
            tipo_membresia: Tipo de membresía (Basica, Estandar, Premium)

        Returns:
            Usuario registrado

        Raises:
            BibliotecaException: Si el DNI ya existe
            ValueError: Si el tipo de membresía es inválido
        """
        if dni in self._usuarios:
            raise BibliotecaException(f"Usuario con DNI {dni} ya existe")

        if tipo_membresia not in self._membresias:
            raise ValueError(f"Tipo de membresía inválido: {tipo_membresia}")

        membresia = self._membresias[tipo_membresia]
        estrategia_multa = self._obtener_estrategia_multa(tipo_membresia)

        usuario = Usuario(
            dni=dni,
            nombre=nombre,
            email=email,
            membresia=membresia,
            estrategia_multa=estrategia_multa
        )

        self._usuarios[dni] = usuario
        return usuario

    def _obtener_estrategia_multa(self, tipo_membresia: str):
        """
        Obtiene la estrategia de multa según tipo de membresía.

        Args:
            tipo_membresia: Tipo de membresía

        Returns:
            Estrategia de multa correspondiente
        """
        estrategias = {
            TIPO_MEMBRESIA_BASICA: MultaEstandarStrategy(),
            TIPO_MEMBRESIA_ESTANDAR: MultaReducidaStrategy(),
            TIPO_MEMBRESIA_PREMIUM: SinMultaStrategy()
        }
        return estrategias[tipo_membresia]

    def buscar_usuario(self, dni: int) -> Optional[Usuario]:
        """
        Busca un usuario por DNI.

        Args:
            dni: DNI del usuario

        Returns:
            Usuario encontrado o None
        """
        return self._usuarios.get(dni)

    def obtener_todos_usuarios(self) -> Dict[int, Usuario]:
        """
        Obtiene todos los usuarios registrados.

        Returns:
            Diccionario de usuarios por DNI
        """
        return self._usuarios.copy()