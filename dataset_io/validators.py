"""Validações das hipóteses de entrada do Merge sort."""

import math
import operator
from collections.abc import Sequence
from typing import Any

from .errors import DatasetValidationError


class ComparableSequenceValidator:
    """Verifica se os valores podem ser comparados de forma básica.

    A validação não consegue provar que uma implementação personalizada de
    comparação é uma ordem total. Ela apenas detecta incompatibilidades claras,
    como dicionários, ``None``, tipos misturados e ``NaN``.
    """

    def __init__(self, *, reject_non_finite: bool = True):
        self._reject_non_finite = reject_non_finite

    def validate(self, values: Sequence[Any]) -> None:
        if not values:
            return

        first = values[0]
        self._check_value(first, 0)

        for index, value in enumerate(values[1:], start=1):
            self._check_value(value, index)
            try:
                operator.lt(first, value)
                operator.lt(value, first)
            except TypeError as error:
                raise DatasetValidationError(
                    "os elementos não são comparáveis entre si; "
                    f"problema no índice {index} ({type(value).__name__})"
                ) from error

    def _check_value(self, value: Any, index: int) -> None:
        if (
            self._reject_non_finite
            and isinstance(value, float)
            and not math.isfinite(value)
        ):
            raise DatasetValidationError(
                f"o valor no índice {index} não é finito: {value!r}"
            )

        try:
            operator.lt(value, value)
        except TypeError as error:
            raise DatasetValidationError(
                f"o valor no índice {index} ({type(value).__name__}) "
                "não possui comparação '<' compatível"
            ) from error
