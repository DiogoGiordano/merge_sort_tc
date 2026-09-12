"""Interfaces pequenas usadas pela camada de preparação de dados."""

from collections.abc import Sequence
from pathlib import Path
from typing import Any, Protocol, TypeVar

T = TypeVar("T")


class RawDatasetReader(Protocol):
    """Lê a estrutura do arquivo sem decidir como converter seus valores."""

    def read(self, path: Path) -> list[Any]:
        """Retorna os valores brutos encontrados no arquivo."""


class ValueConverter(Protocol[T]):
    """Converte um valor bruto para o tipo usado pelo algoritmo."""

    def __call__(self, value: Any) -> T:
        """Converte um valor ou levanta um erro de conversão."""


class DatasetValidator(Protocol[T]):
    """Verifica as hipóteses que os valores precisam satisfazer."""

    def validate(self, values: Sequence[T]) -> None:
        """Valida a sequência ou levanta um erro de validação."""
