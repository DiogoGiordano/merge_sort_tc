"""Leitura, normalização e validação de entradas para o Merge sort.

Este pacote não importa e não executa nenhuma implementação de ordenação.
"""

from .converters import identity, to_float, to_int, to_text
from .errors import (
    DatasetConversionError,
    DatasetError,
    DatasetFormatError,
    DatasetValidationError,
)
from .loader import DatasetLoader
from .models import DatasetMetadata, LoadedDataset
from .readers import CsvColumnReader, JsonListReader, TextLineReader
from .validators import ComparableSequenceValidator

__all__ = [
    "ComparableSequenceValidator",
    "CsvColumnReader",
    "DatasetConversionError",
    "DatasetError",
    "DatasetFormatError",
    "DatasetLoader",
    "DatasetMetadata",
    "DatasetValidationError",
    "JsonListReader",
    "LoadedDataset",
    "TextLineReader",
    "identity",
    "to_float",
    "to_int",
    "to_text",
]
