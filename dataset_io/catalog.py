"""Leitura e validação do catálogo de datasets.

O catálogo é uma fonte de metadados. Ele não lê os arquivos de dados e não
executa a ordenação.
"""

import json
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .errors import DatasetCatalogError

_CATEGORIES = {"valid", "invalid", "external"}
_FORMATS = {"text", "csv", "json", "fixture"}
_VALUE_TYPES = {"text", "float", "int", "raw"}


@dataclass(frozen=True)
class DatasetEntry:
    """Metadados de uma entrada catalogada."""

    id: str
    name: str
    category: str
    format_name: str | None
    value_type: str | None
    path: str | None
    column: str | None
    expected_path: str | None
    source_url: str | None
    description: str
    managed: bool


class DatasetCatalog:
    """Catálogo imutável com resolução segura de caminhos locais."""

    def __init__(
        self,
        source_path: Path,
        root: Path,
        version: int,
        entries: tuple[DatasetEntry, ...],
    ):
        self._source_path = source_path
        self._root = root
        self._version = version
        self._entries = entries
        self._by_id = {entry.id: entry for entry in entries}

    @classmethod
    def from_file(
        cls,
        source: str | Path,
        *,
        root: str | Path | None = None,
    ) -> "DatasetCatalog":
        source_path = Path(source)
        try:
            with source_path.open("r", encoding="utf-8") as file:
                document = json.load(file)
        except (OSError, json.JSONDecodeError) as error:
            raise DatasetCatalogError(
                f"não foi possível ler o catálogo '{source_path}': {error}"
            ) from error

        if not isinstance(document, Mapping):
            raise DatasetCatalogError("o catálogo precisa ser um objeto JSON")

        version = document.get("version")
        if isinstance(version, bool) or not isinstance(version, int) or version < 1:
            raise DatasetCatalogError(
                "o campo 'version' precisa ser um inteiro positivo"
            )

        raw_entries = document.get("datasets")
        if not isinstance(raw_entries, list):
            raise DatasetCatalogError("o campo 'datasets' precisa ser uma lista")

        entries = tuple(
            _parse_entry(raw_entry, index)
            for index, raw_entry in enumerate(raw_entries, start=1)
        )
        ids = [entry.id for entry in entries]
        if len(ids) != len(set(ids)):
            raise DatasetCatalogError("o catálogo possui IDs duplicados")

        root_path = Path(root) if root is not None else source_path.parent.parent
        return cls(
            source_path=source_path.resolve(),
            root=root_path.resolve(),
            version=version,
            entries=entries,
        )

    @property
    def entries(self) -> tuple[DatasetEntry, ...]:
        return self._entries

    @property
    def source_path(self) -> Path:
        return self._source_path

    @property
    def version(self) -> int:
        return self._version

    def get(self, dataset_id: str) -> DatasetEntry:
        try:
            return self._by_id[dataset_id]
        except KeyError as error:
            raise DatasetCatalogError(
                f"dataset com ID '{dataset_id}' não foi encontrado no catálogo"
            ) from error

    def resolve_path(self, entry: DatasetEntry) -> Path | None:
        """Resolve um caminho local e impede que ele escape da raiz catalogada."""

        if entry.path is None:
            return None
        return _resolve_inside_root(self._root, entry.path, entry.id)

    def resolve_expected_path(self, entry: DatasetEntry) -> Path | None:
        if entry.expected_path is None:
            return None
        return _resolve_inside_root(self._root, entry.expected_path, entry.id)


def _parse_entry(raw_entry: Any, index: int) -> DatasetEntry:
    if not isinstance(raw_entry, Mapping):
        raise DatasetCatalogError(f"entrada {index} do catálogo precisa ser um objeto")

    entry_id = _required_text(raw_entry, "id", index)
    name = _required_text(raw_entry, "name", index)
    category = _required_text(raw_entry, "category", index)
    if category not in _CATEGORIES:
        raise DatasetCatalogError(
            f"entrada {entry_id}: categoria inválida '{category}'"
        )

    format_name = _optional_text(raw_entry, "format", index)
    if format_name is not None and format_name not in _FORMATS:
        raise DatasetCatalogError(
            f"entrada {entry_id}: formato inválido '{format_name}'"
        )

    value_type = _optional_text(raw_entry, "value_type", index)
    if value_type is not None and value_type not in _VALUE_TYPES:
        raise DatasetCatalogError(f"entrada {entry_id}: tipo inválido '{value_type}'")

    path = _optional_relative_path(raw_entry, "path", index)
    expected_path = _optional_relative_path(raw_entry, "expected_path", index)
    column = _optional_text(raw_entry, "column", index)
    source_url = _optional_text(raw_entry, "source_url", index)
    description = _required_text(raw_entry, "description", index)

    managed = raw_entry.get("managed", format_name in {"text", "csv", "json"})
    if not isinstance(managed, bool):
        raise DatasetCatalogError(
            f"entrada {entry_id}: o campo 'managed' precisa ser booleano"
        )

    if category == "external":
        if path is not None:
            raise DatasetCatalogError(
                f"entrada {entry_id}: dataset externo não pode possuir caminho local"
            )
        if source_url is None:
            raise DatasetCatalogError(
                f"entrada {entry_id}: dataset externo precisa de 'source_url'"
            )
    else:
        if path is None:
            raise DatasetCatalogError(
                f"entrada {entry_id}: dataset local precisa de 'path'"
            )
        if format_name is None or value_type is None:
            raise DatasetCatalogError(
                f"entrada {entry_id}: dataset local precisa de 'format' e 'value_type'"
            )
        if format_name == "csv" and column is None:
            raise DatasetCatalogError(
                f"entrada {entry_id}: CSV precisa informar a coluna"
            )

    return DatasetEntry(
        id=entry_id,
        name=name,
        category=category,
        format_name=format_name,
        value_type=value_type,
        path=path,
        column=column,
        expected_path=expected_path,
        source_url=source_url,
        description=description,
        managed=managed,
    )


def _required_text(record: Mapping[str, Any], field: str, index: int) -> str:
    value = record.get(field)
    if not isinstance(value, str) or not value.strip():
        raise DatasetCatalogError(
            f"entrada {index}: o campo '{field}' precisa ser texto não vazio"
        )
    return value.strip()


def _optional_text(record: Mapping[str, Any], field: str, index: int) -> str | None:
    value = record.get(field)
    if value is None:
        return None
    if not isinstance(value, str) or not value.strip():
        raise DatasetCatalogError(
            f"entrada {index}: o campo '{field}' precisa ser texto ou nulo"
        )
    return value.strip()


def _optional_relative_path(
    record: Mapping[str, Any], field: str, index: int
) -> str | None:
    value = _optional_text(record, field, index)
    if value is None:
        return None
    path = Path(value)
    if path.is_absolute() or ".." in path.parts:
        raise DatasetCatalogError(
            f"entrada {index}: o campo '{field}' precisa ser um caminho relativo seguro"
        )
    return path.as_posix()


def _resolve_inside_root(root: Path, relative_path: str, entry_id: str) -> Path:
    root_path = root.resolve()
    candidate = (root_path / relative_path).resolve()
    try:
        candidate.relative_to(root_path)
    except ValueError as error:
        raise DatasetCatalogError(
            f"entrada {entry_id}: caminho fora da raiz do catálogo"
        ) from error
    return candidate
