"""Serviço que coordena leitura, conversão e validação."""

from pathlib import Path
from typing import Generic, TypeVar

from .errors import DatasetConversionError, DatasetError
from .interfaces import DatasetValidator, RawDatasetReader, ValueConverter
from .models import DatasetMetadata, LoadedDataset

T = TypeVar("T")


class DatasetLoader(Generic[T]):
    """Transforma um arquivo em uma lista validada, sem ordenar seus valores."""

    def __init__(
        self,
        reader: RawDatasetReader,
        converter: ValueConverter[T],
        validator: DatasetValidator[T] | None = None,
        *,
        format_name: str,
    ):
        self._reader = reader
        self._converter = converter
        self._validator = validator
        self._format_name = format_name

    def load(
        self,
        source: str | Path,
        *,
        name: str | None = None,
        column: str | None = None,
        transformations: tuple[str, ...] = (),
    ) -> LoadedDataset[T]:
        path = Path(source)
        raw_values = self._reader.read(path)
        values: list[T] = []

        for index, raw_value in enumerate(raw_values, start=1):
            try:
                values.append(self._converter(raw_value))
            except DatasetError as error:
                raise DatasetConversionError(
                    f"{path}, item {index}: {error}"
                ) from error
            except (TypeError, ValueError) as error:
                raise DatasetConversionError(
                    f"{path}, item {index}: não foi possível converter {raw_value!r}"
                ) from error

        if self._validator is not None:
            self._validator.validate(values)

        metadata = DatasetMetadata(
            name=name or path.stem,
            source=path,
            format_name=self._format_name,
            column=column,
            transformations=transformations,
        )
        return LoadedDataset(metadata=metadata, values=values)
