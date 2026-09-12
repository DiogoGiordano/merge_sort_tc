"""Formatadores de saída para humanos e para automação."""

import json
from typing import Any

from .management import DatasetInspection, DatasetSummary

_CATEGORY_LABELS = {
    "valid": "válida",
    "invalid": "inválida",
    "external": "externa",
}
_AVAILABILITY_LABELS = {
    "local": "local",
    "missing": "ausente",
    "external": "externa",
}
_STATUS_LABELS = {
    "valid": "válido",
    "invalid": "inválido",
    "external": "externo",
    "missing": "ausente",
    "unsupported": "não gerenciado",
}


def format_catalog_text(summaries: tuple[DatasetSummary, ...]) -> str:
    headers = ("ID", "Nome", "Categoria", "Disponibilidade", "Formato", "Tipo")
    rows = [
        (
            summary.entry.id,
            summary.entry.name,
            _CATEGORY_LABELS[summary.entry.category],
            _AVAILABILITY_LABELS[summary.availability],
            summary.entry.format_name or "-",
            summary.entry.value_type or "-",
        )
        for summary in summaries
    ]
    widths = [
        max(len(row[index]) for row in (headers, *rows))
        for index in range(len(headers))
    ]
    lines = [
        "  ".join(value.ljust(widths[index]) for index, value in enumerate(headers)),
        "  ".join("-" * width for width in widths),
    ]
    lines.extend(
        "  ".join(value.ljust(widths[index]) for index, value in enumerate(row))
        for row in rows
    )
    return "\n".join(lines)


def format_catalog_json(version: int, summaries: tuple[DatasetSummary, ...]) -> str:
    document = {
        "catalog_version": version,
        "datasets": [_summary_record(summary) for summary in summaries],
    }
    return _dump(document)


def format_inspection_text(
    result: DatasetInspection,
    *,
    include_sample: bool = True,
) -> str:
    entry = result.entry
    lines = [
        f"ID: {entry.id}",
        f"Nome: {entry.name}",
        f"Categoria declarada: {_CATEGORY_LABELS[entry.category]}",
        f"Disponibilidade: {_AVAILABILITY_LABELS[result.availability]}",
        f"Formato: {entry.format_name or '-'}",
        f"Tipo: {entry.value_type or '-'}",
        f"Fonte local: {entry.path or '-'}",
    ]
    if entry.column is not None:
        lines.append(f"Coluna: {entry.column}")
    if entry.expected_path is not None:
        lines.append(f"Saída esperada: {entry.expected_path}")
    if entry.source_url is not None:
        lines.append(f"Fonte externa: {entry.source_url}")
    if result.count is not None:
        lines.append(f"Quantidade: {result.count}")
        if include_sample:
            lines.append(f"Amostra: {list(result.sample)!r}")
    lines.append(f"Status observado: {_STATUS_LABELS[result.status]}")
    if result.status == "external":
        lines.append("Download: não realizado")
    if result.error is not None:
        lines.append(f"Detalhe: {result.error}")
    return "\n".join(lines)


def format_inspection_json(
    result: DatasetInspection,
    *,
    include_sample: bool = True,
) -> str:
    return _dump(_inspection_record(result, include_sample=include_sample))


def format_error_json(error: Exception) -> str:
    return _dump({"status": "error", "error": str(error)})


def _summary_record(summary: DatasetSummary) -> dict[str, Any]:
    entry = summary.entry
    return {
        "id": entry.id,
        "name": entry.name,
        "category": entry.category,
        "availability": summary.availability,
        "managed": entry.managed,
        "format": entry.format_name,
        "value_type": entry.value_type,
        "path": entry.path,
        "column": entry.column,
        "expected_path": entry.expected_path,
        "source_url": entry.source_url,
        "description": entry.description,
    }


def _inspection_record(
    result: DatasetInspection,
    *,
    include_sample: bool,
) -> dict[str, Any]:
    entry = result.entry
    return {
        "id": entry.id,
        "name": entry.name,
        "declared_category": entry.category,
        "availability": result.availability,
        "managed": entry.managed,
        "format": entry.format_name,
        "value_type": entry.value_type,
        "path": entry.path,
        "column": entry.column,
        "expected_path": entry.expected_path,
        "source_url": entry.source_url,
        "status": result.status,
        "count": result.count,
        "sample": list(result.sample) if include_sample else None,
        "error": result.error,
    }


def _dump(document: dict[str, Any]) -> str:
    return json.dumps(document, ensure_ascii=False, indent=2)
