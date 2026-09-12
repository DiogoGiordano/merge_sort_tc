
import random
from time import perf_counter

from algorithms.merge_sort_recursive import merge_sort_recursive
from algorithms.merge_sort_iterative import merge_sort_iterative
from cli.arguments import parse_arguments
from cli.console import error, success
from core.logging_config import setup_logging


def create_vector(args) -> list[int]:
    if args.values is not None:
        return args.values.copy()

    if args.random is None:
        raise ValueError(
            "É necessário informar --values ou --random."
        )

    if args.random <= 0:
        raise ValueError("--random deve ser maior que zero")

    if args.minimum > args.maximum:
        raise ValueError("--min não pode ser maior que --max")

    generator = random.Random(args.seed)

    return [
        generator.randint(args.minimum, args.maximum)
        for _ in range(args.random)
    ]


def main() -> None:
    args = parse_arguments()
    print(args.log_level.upper())

    logger = setup_logging(
        args.log_level.upper(),
        log_file=args.log_file,
    )

    try:
        vector = create_vector(args)

        logger.info("Vetor recebido: %s", vector)
        logger.info("Quantidade de elementos: %d", len(vector))

        start = perf_counter()

        ordered = merge_sort_recursive(vector)

        if args.descending:
            ordered.reverse()

        elapsed = perf_counter() - start

        success(f"Vetor original: {vector}")
        success(f"Vetor ordenado: {ordered}")

        if args.metrics:
            print(f"Tempo: {elapsed:.8f} segundos")
            print(f"Elementos: {len(vector)}")

    except ValueError as exception:
        logger.error("%s", exception)
        error(str(exception))


if __name__ == "__main__":
    main()