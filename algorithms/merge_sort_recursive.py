import logging
from .merge_base import merge

logger = logging.getLogger("merge_sort")

def merge_sort_recursive(values: list[int], depth: int = 0) -> list[int]:
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
        return values

    middle = len(values) // 2

    left = merge_sort_recursive(values[:middle], depth + 1)
    right = merge_sort_recursive(values[middle:], depth + 1)

    result = merge(left, right)

    logger.debug(
        "Profundidade %d: merge %s + %s -> %s",
        depth,
        left,
        right,
        result,
    )

    return result
