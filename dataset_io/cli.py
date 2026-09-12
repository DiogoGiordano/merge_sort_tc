"""Interface de linha de comando para leitura e gerenciamento de datasets.

O modo legado recebe diretamente o caminho de um arquivo. O modo de
gerenciamento começa com ``datasets`` e trabalha com os IDs do catálogo.
Nenhum dos dois modos executa a ordenação.
"""

import argparse
import sys
from pathlib import Path

from .catalog import DatasetCatalog
from .errors import DatasetError
from .factories import build_converter, build_reader
from .formatters import (
    format_catalog_json,
    format_catalog_text,
    format_error_json,
    format_inspection_json,
    format_inspection_text,
)
from .loader import DatasetLoader
from .management import DatasetInspection, DatasetManager
from .validators import ComparableSequenceValidator


def _default_catalog_path() -> Path:
    return Path(__file__).resolve().parent.parent / "datasets" / "catalogo.json"


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Lê e valida uma entrada sem executar a ordenação.",
        epilog=(
            "Gerenciamento por catálogo: python3 -m dataset_io.cli datasets list\n"
            "Consulte dataset_io/README.md para os subcomandos disponíveis."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
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


def _build_management_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python3 -m dataset_io.cli datasets",
        description="Lista, inspeciona e valida entradas do catálogo.",
    )
    parser.add_argument(
        "--catalog",
        type=Path,
        default=_default_catalog_path(),
        help="caminho do catálogo JSON (padrão: datasets/catalogo.json)",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    list_parser = subparsers.add_parser(
        "list",
        help="lista datasets locais, inválidos e externos",
    )
    _add_catalog_argument(list_parser)
    _add_output_argument(list_parser)

    inspect_parser = subparsers.add_parser(
        "inspect",
        help="mostra metadados e uma amostra de um dataset",
    )
    _add_catalog_argument(inspect_parser)
    inspect_parser.add_argument("dataset_id", help="ID cadastrado no catálogo")
    inspect_parser.add_argument(
        "--sample",
        type=int,
        default=10,
        help="quantidade de valores exibidos (padrão: 10)",
    )
    _add_output_argument(inspect_parser)

    validate_parser = subparsers.add_parser(
        "validate",
        help="valida uma entrada local contra as restrições",
    )
    _add_catalog_argument(validate_parser)
    validate_parser.add_argument("dataset_id", help="ID cadastrado no catálogo")
    _add_output_argument(validate_parser)

    return parser


def _add_catalog_argument(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--catalog",
        type=Path,
        default=argparse.SUPPRESS,
        help="caminho alternativo do catálogo JSON",
    )


def _add_output_argument(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--output",
        choices=("text", "json"),
        default="text",
        help="formato da saída (padrão: text)",
    )


def _run_legacy(argv: list[str]) -> int:
    args = _build_parser().parse_args(argv)
    if args.sample < 0:
        print("ERRO: --sample não pode ser negativo", file=sys.stderr)
        return 2

    try:
        reader, format_name = build_reader(args.file_format, args.column)
        converter, transformations = build_converter(args.value_type)
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


def _run_management(argv: list[str]) -> int:
    parser = _build_management_parser()
    args = parser.parse_args(argv)

    try:
        catalog = DatasetCatalog.from_file(args.catalog)
        manager = DatasetManager(catalog)

        if args.command == "list":
            summaries = manager.list_entries()
            if args.output == "json":
                print(format_catalog_json(catalog.version, summaries))
            else:
                print(format_catalog_text(summaries))
            return 0

        if args.command == "inspect":
            result = manager.inspect(args.dataset_id, sample=args.sample)
            _print_inspection(result, args.output, include_sample=True)
            return _inspection_exit_code(result)

        result = manager.validate(args.dataset_id)
        _print_inspection(result, args.output, include_sample=False)
        return _validation_exit_code(result)
    except (DatasetError, ValueError) as error:
        if args.output == "json":
            print(format_error_json(error))
        else:
            print(f"ERRO: {error}", file=sys.stderr)
        return 2


def _print_inspection(
    result: DatasetInspection,
    output: str,
    *,
    include_sample: bool,
) -> None:
    if output == "json":
        print(format_inspection_json(result, include_sample=include_sample))
    else:
        print(format_inspection_text(result, include_sample=include_sample))


def _inspection_exit_code(result: DatasetInspection) -> int:
    if result.status in {"valid", "invalid", "external"}:
        return 0
    return 2


def _validation_exit_code(result: DatasetInspection) -> int:
    if result.status == "valid":
        return 0
    if result.status == "invalid":
        return 1
    return 2


def main(argv: list[str] | None = None) -> int:
    arguments = list(sys.argv[1:] if argv is None else argv)
    if arguments and arguments[0] == "datasets":
        return _run_management(arguments[1:])
    return _run_legacy(arguments)


if __name__ == "__main__":
    raise SystemExit(main())
