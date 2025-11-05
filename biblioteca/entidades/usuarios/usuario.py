"""
Entidad Usuario del sistema.
Representa un usuario de la biblioteca.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from biblioteca_digital.entidades.usuarios.membresia import Membresia
    from biblioteca_digital.patrones.strategy.multa_strategy import MultaStrategy


class Usuario:
    """
    Representa un usuario de la biblioteca.
    Usa Strategy Pattern para el cálculo de multas.
    """

    def __init__(
        self,
        dni: int,
        nombre: str,
        email: str,
        membresia: 'Membresia',
        estrategia_multa: 'MultaStrategy'
    ):
        """
        Inicializa un usuario.

        Args:
            dni: DNI único del usuario
            nombre: Nombre completo
            email: Email de contacto
            membresia: Tipo de membresía
            estrategia_multa: Estrategia para calcular multas

        Raises:
            ValueError: Si el DNI es inválido
        """
        if dni <= 0:
            raise ValueError("El DNI debe ser un número positivo")

        self._dni = dni
        self._nombre = nombre
        self._email = email
        self._membresia = membresia
        self._estrategia_multa = estrategia_multa

    def get_dni(self) -> int:
        """Retorna el DNI del usuario."""
        return self._dni

    def get_nombre(self) -> str:
        """Retorna el nombre del usuario."""
        return self._nombre

    def get_email(self) -> str:
        """Retorna el email del usuario."""
        return self._email

    def get_membresia(self) -> 'Membresia':
        """Retorna la membresía del usuario."""
        return self._membresia

    def calcular_multa(self, dias_retraso: int) -> float:
        """
        Calcula la multa por días de retraso.
        Delega el cálculo a la estrategia inyectada.

        Args:
            dias_retraso: Número de días de retraso

        Returns:
            Monto de la multa
        """
        return self._estrategia_multa.calcular_multa(dias_retraso)

    def __str__(self) -> str:
        """Representación en string."""
        return f"Usuario: {self._nombre} (DNI: {self._dni}) - {self._membresia.get_tipo()}"

    def __repr__(self) -> str:
        """Representación técnica."""
        return f"Usuario(dni={self._dni}, nombre='{self._nombre}')"