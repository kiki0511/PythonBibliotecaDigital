"""
Archivo integrador generado automaticamente
Directorio: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/servicios/usuarios
Fecha: 2025-11-05 09:05:45
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: usuario_manager.py
# Ruta: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/servicios/usuarios/usuario_manager.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 2/2: usuario_service.py
# Ruta: /Users/pc_joaco/Desktop/Facu/3-Diseno_de_sistema/PythonBibliotecaDigital/biblioteca_digital/servicios/usuarios/usuario_service.py
# ================================================================================

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


