"""Interface simples para inspecionar datasets preparados.

Uso típico, a partir da raiz do repositório:

    python3 -m dataset_io.cli datasets/validos/iris_petal_length.txt \
        --format text --type float

Esta interface apenas lê, converte e valida. Ela não chama o Merge sort.
"""

import argparse
import sys
from collections.abc import Callable
from pathlib import Path
from typing import Any

from .converters import identity, to_float, to_int, to_text
from .errors import DatasetError
from .loader import DatasetLoader
from .readers import CsvColumnReader, JsonListReader, TextLineReader
from .validators import ComparableSequenceValidator


def _build_reader(file_format: str, column: str | None) -> tuple[Any, str]:
    if file_format == "text":
        return TextLineReader(), TextLineReader.format_name
    if file_format == "csv":
        if column is None:
            raise ValueError("--column é obrigatório para arquivos CSV")
        return CsvColumnReader(column), CsvColumnReader.format_name
    if file_format == "json":
        return JsonListReader(), JsonListReader.format_name
    raise ValueError(f"formato não suportado: {file_format}")


def _build_converter(value_type: str) -> tuple[Callable[[Any], Any], tuple[str, ...]]:
    if value_type == "text":
        return to_text, ("remoção de espaços externos",)
    if value_type == "float":
        return to_float, ("conversão para float", "rejeição de valores não finitos")
    if value_type == "int":
        return to_int, ("conversão para int",)
    if value_type == "raw":
        return identity, ()
    raise ValueError(f"tipo não suportado: {value_type}")


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Lê e valida uma entrada sem executar a ordenação."
    )
    parser.add_argument("path", type=Path, help="caminho do dataset")
    parser.add_argument(
        "--format",
        choices=("text", "csv", "json"),
        required=True,
        dest="file_format",
        help="formato estrutural do arquivo",
    )
    parser.add_argument(
        "--type",
        choices=("text", "float", "int", "raw"),
        required=True,
        dest="value_type",
        help="tipo dos valores entregues ao algoritmo",
    )
    parser.add_argument(
        "--column",
        help="nome da coluna; obrigatório para CSV",
    )
    parser.add_argument(
        "--sample",
        type=int,
        default=10,
        help="quantidade de valores exibidos (padrão: 10)",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    if args.sample < 0:
        print("ERRO: --sample não pode ser negativo", file=sys.stderr)
        return 2

    try:
        reader, format_name = _build_reader(args.file_format, args.column)
        converter, transformations = _build_converter(args.value_type)
        loader = DatasetLoader(
            reader,
            converter,
            ComparableSequenceValidator(),
            format_name=format_name,
        )
        dataset = loader.load(
            args.path,
            column=args.column,
            transformations=transformations,
        )
    except (DatasetError, ValueError) as error:
        print(f"ERRO: {error}", file=sys.stderr)
        return 2

    metadata = dataset.metadata
    print(f"Nome: {metadata.name}")
    print(f"Fonte: {metadata.source}")
    print(f"Formato: {metadata.format_name}")
    if metadata.column is not None:
        print(f"Coluna: {metadata.column}")
    print(f"Quantidade: {len(dataset.values)}")
    print(f"Amostra: {dataset.values[: args.sample]!r}")
    print("Status: entrada compatível com a camada de leitura")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
