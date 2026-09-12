"""Serviço de catálogo, inspeção e validação de datasets."""

from dataclasses import dataclass
from typing import Any

from .catalog import DatasetCatalog, DatasetEntry
from .errors import DatasetError
from .factories import build_loader


@dataclass(frozen=True)
class DatasetSummary:
    """Resumo usado pelo comando de listagem."""

    entry: DatasetEntry
    availability: str


@dataclass(frozen=True)
class DatasetInspection:
    """Resultado de uma inspeção sem efeitos colaterais."""

    entry: DatasetEntry
    availability: str
    status: str
    count: int | None = None
    sample: tuple[Any, ...] = ()
    error: str | None = None


class DatasetManager:
    """Orquestra o catálogo e o carregamento sem executar a ordenação."""

    def __init__(self, catalog: DatasetCatalog):
        self._catalog = catalog

    @property
    def catalog(self) -> DatasetCatalog:
        return self._catalog

    def list_entries(self) -> tuple[DatasetSummary, ...]:
        summaries = (
            DatasetSummary(entry, self._availability(entry))
            for entry in self._catalog.entries
        )
        return tuple(sorted(summaries, key=lambda summary: summary.entry.id))

    def inspect(self, dataset_id: str, *, sample: int = 10) -> DatasetInspection:
        if sample < 0:
            raise ValueError("a quantidade da amostra não pode ser negativa")

        entry = self._catalog.get(dataset_id)
        availability = self._availability(entry)

        if availability == "external":
            return DatasetInspection(entry, availability, "external")
        if availability == "missing":
            return DatasetInspection(
                entry,
                availability,
                "missing",
                error=f"arquivo local não encontrado: {entry.path}",
            )
        if not entry.managed:
            return DatasetInspection(
                entry,
                availability,
                "unsupported",
                error="esta entrada é uma fixture e não possui leitor gerenciado",
            )
        if entry.format_name is None or entry.value_type is None:
            return DatasetInspection(
                entry,
                availability,
                "unsupported",
                error="a entrada não possui formato e tipo para o carregador",
            )

        path = self._catalog.resolve_path(entry)
        if path is None:
            return DatasetInspection(
                entry,
                "missing",
                "missing",
                error="a entrada local não possui caminho",
            )

        try:
            loader = build_loader(entry.format_name, entry.value_type, entry.column)
            loaded = loader.load(
                path,
                name=entry.name,
                column=entry.column,
            )
        except DatasetError as error:
            return DatasetInspection(
                entry,
                availability,
                "invalid",
                error=str(error),
            )
        except ValueError as error:
            return DatasetInspection(
                entry,
                availability,
                "invalid",
                error=str(error),
            )

        return DatasetInspection(
            entry,
            availability,
            "valid",
            count=len(loaded.values),
            sample=tuple(loaded.values[:sample]),
        )

    def validate(self, dataset_id: str) -> DatasetInspection:
        """Valida uma entrada e não inclui amostra no resultado."""

        return self.inspect(dataset_id, sample=0)

    def _availability(self, entry: DatasetEntry) -> str:
        if entry.category == "external":
            return "external"
        path = self._catalog.resolve_path(entry)
        if path is not None and path.is_file():
            return "local"
        return "missing"
