"""Fábricas compartilhadas pela CLI legada e pelo gerenciamento."""

from collections.abc import Callable
from typing import Any

from .converters import identity, to_float, to_int, to_text
from .interfaces import RawDatasetReader
from .loader import DatasetLoader
from .readers import CsvColumnReader, JsonListReader, TextLineReader
from .validators import ComparableSequenceValidator


def build_reader(file_format: str, column: str | None) -> tuple[RawDatasetReader, str]:
    """Cria o leitor correspondente ao formato informado."""

    if file_format == "text":
        return TextLineReader(), TextLineReader.format_name
    if file_format == "csv":
        if column is None:
            raise ValueError("--column é obrigatório para arquivos CSV")
        return CsvColumnReader(column), CsvColumnReader.format_name
    if file_format == "json":
        return JsonListReader(), JsonListReader.format_name
    raise ValueError(f"formato não suportado: {file_format}")


def build_converter(
    value_type: str,
) -> tuple[Callable[[Any], Any], tuple[str, ...]]:
    """Cria o conversor correspondente ao tipo da entrada."""

    if value_type == "text":
        return to_text, ("remoção de espaços externos",)
    if value_type == "float":
        return to_float, ("conversão para float", "rejeição de valores não finitos")
    if value_type == "int":
        return to_int, ("conversão para int",)
    if value_type == "raw":
        return identity, ()
    raise ValueError(f"tipo não suportado: {value_type}")


def build_loader(
    file_format: str,
    value_type: str,
    column: str | None,
) -> DatasetLoader[Any]:
    reader, format_name = build_reader(file_format, column)
    converter, _ = build_converter(value_type)
    return DatasetLoader(
        reader,
        converter,
        ComparableSequenceValidator(),
        format_name=format_name,
    )
