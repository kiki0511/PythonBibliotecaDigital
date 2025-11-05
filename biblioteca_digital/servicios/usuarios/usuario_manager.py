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
