"""Erros específicos da camada de leitura de datasets."""


class DatasetError(Exception):
    """Erro-base para falhas esperadas durante a preparação de dados."""


class DatasetFormatError(DatasetError):
    """O arquivo não possui o formato ou a coluna esperada."""


class DatasetCatalogError(DatasetError):
    """O catálogo não possui uma estrutura ou entrada válida."""


class DatasetConversionError(DatasetError):
    """Um valor não pôde ser convertido para o tipo solicitado."""


class DatasetValidationError(DatasetError):
    """Os valores violam as hipóteses de entrada do Merge sort."""
