"""Leitores de formatos de arquivo.

Cada leitor conhece somente a estrutura do seu formato. Conversão de tipos e
validação de comparabilidade ficam em componentes separados.
"""

import csv
import json
from pathlib import Path
from typing import Any

from .errors import DatasetFormatError


class TextLineReader:
    """Lê um valor textual por linha, ignorando linhas vazias por padrão."""

    format_name = "text"

    def __init__(self, *, encoding: str = "utf-8", ignore_blank_lines: bool = True):
        self._encoding = encoding
        self._ignore_blank_lines = ignore_blank_lines

    def read(self, path: Path) -> list[Any]:
        try:
            with path.open("r", encoding=self._encoding) as file:
                values = []
                for line in file:
                    value = line.strip()
                    if not value and self._ignore_blank_lines:
                        continue
                    values.append(value)
                return values
        except OSError as error:
            raise DatasetFormatError(
                f"não foi possível ler '{path}': {error}"
            ) from error


class CsvColumnReader:
    """Lê uma coluna nomeada de um CSV com cabeçalho."""

    format_name = "csv"

    def __init__(
        self,
        column: str,
        *,
        delimiter: str = ",",
        encoding: str = "utf-8-sig",
    ):
        if not column.strip():
            raise ValueError("a coluna do CSV não pode ser vazia")
        if len(delimiter) != 1:
            raise ValueError("o delimitador do CSV deve possuir um caractere")

        self._column = column
        self._delimiter = delimiter
        self._encoding = encoding

    def read(self, path: Path) -> list[Any]:
        try:
            with path.open("r", newline="", encoding=self._encoding) as file:
                reader = csv.DictReader(file, delimiter=self._delimiter)

                if not reader.fieldnames:
                    raise DatasetFormatError(f"'{path}' não possui um cabeçalho CSV")
                if self._column not in reader.fieldnames:
                    available = ", ".join(reader.fieldnames)
                    raise DatasetFormatError(
                        f"coluna '{self._column}' não encontrada em '{path}'; "
                        f"colunas disponíveis: {available}"
                    )

                values = []
                for line_number, row in enumerate(reader, start=2):
                    value = row.get(self._column)
                    if value is None or not value.strip():
                        raise DatasetFormatError(
                            f"valor ausente na coluna '{self._column}' "
                            f"na linha {line_number} de '{path}'"
                        )
                    values.append(value.strip())
                return values
        except DatasetFormatError:
            raise
        except (OSError, csv.Error) as error:
            raise DatasetFormatError(
                f"não foi possível ler '{path}': {error}"
            ) from error


class JsonListReader:
    """Lê um arquivo JSON cujo elemento de nível superior é uma lista."""

    format_name = "json"

    def __init__(self, *, encoding: str = "utf-8"):
        self._encoding = encoding

    def read(self, path: Path) -> list[Any]:
        try:
            with path.open("r", encoding=self._encoding) as file:
                data = json.load(file)
        except (OSError, json.JSONDecodeError) as error:
            raise DatasetFormatError(
                f"não foi possível ler o JSON '{path}': {error}"
            ) from error

        if not isinstance(data, list):
            raise DatasetFormatError(
                f"o JSON '{path}' precisa conter uma lista no nível superior"
            )
        return data
