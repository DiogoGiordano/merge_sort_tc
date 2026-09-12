"""Modelos de dados retornados pelo carregador."""

from dataclasses import dataclass
from pathlib import Path
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass(frozen=True)
class DatasetMetadata:
    """Metadados suficientes para reproduzir a preparação de uma entrada."""

    name: str
    source: Path
    format_name: str
    column: str | None = None
    transformations: tuple[str, ...] = ()


@dataclass(frozen=True)
class LoadedDataset(Generic[T]):
    """Uma entrada normalizada, pronta para ser entregue ao algoritmo."""

    metadata: DatasetMetadata
    values: list[T]
