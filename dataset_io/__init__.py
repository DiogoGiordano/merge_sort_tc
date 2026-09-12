"""Leitura, normalização e validação de entradas para o Merge sort.

Este pacote não importa e não executa nenhuma implementação de ordenação.
"""

from .catalog import DatasetCatalog, DatasetEntry
from .converters import identity, to_float, to_int, to_text
from .errors import (
    DatasetCatalogError,
    DatasetConversionError,
    DatasetError,
    DatasetFormatError,
    DatasetValidationError,
)
from .loader import DatasetLoader
from .management import DatasetInspection, DatasetManager, DatasetSummary
from .models import DatasetMetadata, LoadedDataset
from .readers import CsvColumnReader, JsonListReader, TextLineReader
from .validators import ComparableSequenceValidator

__all__ = [
    "ComparableSequenceValidator",
    "CsvColumnReader",
    "DatasetCatalog",
    "DatasetCatalogError",
    "DatasetConversionError",
    "DatasetEntry",
    "DatasetError",
    "DatasetFormatError",
    "DatasetInspection",
    "DatasetLoader",
    "DatasetManager",
    "DatasetMetadata",
    "DatasetSummary",
    "DatasetValidationError",
    "JsonListReader",
    "LoadedDataset",
    "TextLineReader",
    "identity",
    "to_float",
    "to_int",
    "to_text",
]
