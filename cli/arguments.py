
import argparse


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="merge-sort",
        description="Ordenação e análise de vetores usando Merge Sort.",
    )

    input_group = parser.add_mutually_exclusive_group(required=True)

    input_group.add_argument(
        "--values",
        nargs="+",
        type=int,
        metavar="N",
        help="Valores que serão ordenados.",
    )

    input_group.add_argument(
        "--random",
        type=int,
        metavar="QUANTIDADE",
        help="Gera um vetor aleatório com a quantidade informada.",
    )

    parser.add_argument(
        "--type",
        type=int,
        default=1,
        help="Tipo de funcionamento do algoritmo.",
    )

    parser.add_argument(
        "--min",
        type=int,
        default=1,
        dest="minimum",
        help="Menor valor da geração aleatória. Padrão: 0.",
    )

    parser.add_argument(
        "--max",
        type=int,
        default=100,
        dest="maximum",
        help="Maior valor da geração aleatória. Padrão: 100.",
    )

    parser.add_argument(
        "--seed",
        type=int,
        help="Semente para repetir a mesma geração aleatória.",
    )

    parser.add_argument(
        "--log-level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        default="WARNING",
        help="Nível de log. Padrão: WARNING.",
    )

    parser.add_argument(
        "--log-file",
        type=str,
        metavar="ARQUIVO",
        help="Arquivo em que os logs serão salvos.",
    )

    parser.add_argument(
        "--metrics",
        action="store_true",
        help="Exibe métricas da ordenação.",
    )

    parser.add_argument(
        "--visualize",
        action="store_true",
        help="Exibe a ordenação passo a passo.",
    )

    parser.add_argument(
        "--delay",
        type=float,
        default=0.2,
        help="Intervalo da visualização em segundos. Padrão: 0.2.",
    )

    parser.add_argument(
        "--descending",
        action="store_true",
        help="Ordena do maior para o menor.",
    )

    parser.add_argument(
        "--repeat",
        type=int,
        default=1,
        help="Quantidade de execuções. Padrão: 1.",
    )

    return parser.parse_args()