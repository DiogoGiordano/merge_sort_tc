"""Conversores de valores brutos para tipos aceitos pelo algoritmo."""

import math
from typing import Any

from .errors import DatasetConversionError


def identity(value: Any) -> Any:
    """Mantém o valor original, útil para validar JSONs heterogêneos."""

    return value


def to_text(value: Any) -> str:
    """Aceita somente texto não vazio e remove espaços externos."""

    if not isinstance(value, str):
        raise DatasetConversionError(
            f"esperava texto, mas recebeu {type(value).__name__}"
        )

    normalized = value.strip()
    if not normalized:
        raise DatasetConversionError("texto vazio não é um valor de dataset")
    return normalized


def to_float(value: Any) -> float:
    """Converte para float e rejeita valores não finitos, como NaN."""

    try:
        normalized = float(value)
    except (TypeError, ValueError) as error:
        raise DatasetConversionError(
            f"não foi possível converter {value!r} para float"
        ) from error

    if not math.isfinite(normalized):
        raise DatasetConversionError(f"o valor {value!r} não é um número finito")
    return normalized


def to_int(value: Any) -> int:
    """Converte somente valores inteiros, sem truncar frações silenciosamente."""

    if isinstance(value, bool):
        raise DatasetConversionError("booleanos não são aceitos como inteiros")

    try:
        normalized = int(value)
    except (TypeError, ValueError) as error:
        raise DatasetConversionError(
            f"não foi possível converter {value!r} para int"
        ) from error

    if isinstance(value, float) and not value.is_integer():
        raise DatasetConversionError(f"o valor {value!r} possui parte fracionária")
    if isinstance(value, str) and str(normalized) != value.strip():
        raise DatasetConversionError(
            f"o texto {value!r} não representa um inteiro puro"
        )
    return normalized
