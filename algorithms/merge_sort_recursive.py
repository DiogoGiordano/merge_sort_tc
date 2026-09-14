import logging
from .merge_base import merge


logger = logging.getLogger("merge_sort")


def merge_sort_recursive(
    values: list[int],
    depth: int = 0,
    metrics: dict | None = None,
) -> tuple[list[int], dict]:
    """
    Ordena um vetor usando Merge Sort recursivo.

    Args:
        values: Vetor que será ordenado.
        depth: Profundidade atual da recursão.
        metrics: Contadores de comparações e movimentos.

    Returns:
        Vetor ordenado e as métricas de comparações e movimentos.
    """

    if metrics is None:
        metrics = {"comparisons": 0, "movements": 0}

    logger.debug(
        "Profundidade %d: processando %s",
        depth,
        values,
    )

    if len(values) <= 1:
        logger.debug(
            "Profundidade %d: caso-base %s",
            depth,
            values,
        )
        return values, metrics

    middle = len(values) // 2

    left, metrics = merge_sort_recursive(
        values[:middle],
        depth + 1,
        metrics,
    )

    right, metrics = merge_sort_recursive(
        values[middle:],
        depth + 1,
        metrics,
    )

    result = merge(left, right, metrics)

    logger.debug(
        "Profundidade %d: merge %s + %s -> %s",
        depth,
        left,
        right,
        result,
    )

    return result, metrics