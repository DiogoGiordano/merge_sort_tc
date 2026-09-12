# Camada de leitura dos datasets

Esta camada prepara entradas para o Merge sort, mas não implementa nem chama a
ordenação. A saída do carregador é uma lista validada, que os colegas podem
entregar à função de ordenação existente.

## Responsabilidades

| Componente | Responsabilidade |
| --- | --- |
| `readers.py` | Entender TXT, CSV e JSON e extrair valores brutos |
| `converters.py` | Transformar texto, números e valores JSON em tipos definidos |
| `validators.py` | Detectar incompatibilidades de comparação e valores não finitos |
| `loader.py` | Orquestrar leitura, conversão, validação e metadados |
| `models.py` | Representar metadados e a lista carregada |
| `cli.py` | Permitir inspeção manual sem acoplar o algoritmo |
| `errors.py` | Padronizar mensagens de falha |

## Relação com SOLID

- **Responsabilidade única:** leitor, conversor, validador e orquestrador têm
  tarefas distintas.
- **Aberto/fechado:** novos formatos podem implementar `RawDatasetReader` sem
  alterar o serviço de carregamento.
- **Substituição de Liskov:** qualquer leitor compatível pode ser injetado no
  `DatasetLoader`.
- **Segregação de interfaces:** as interfaces são pequenas e específicas.
- **Inversão de dependência:** `DatasetLoader` depende das interfaces de leitor,
  conversor e validador, não de um formato concreto.

## Comandos de inspeção

Os comandos devem ser executados na raiz do projeto.

### Iris numérico

```text
python3 -m dataset_io.cli datasets/validos/iris_petal_length.txt --format text --type float
```

### Iris textual

```text
python3 -m dataset_io.cli datasets/validos/iris_classes.txt --format text --type text
```

### Iris CSV, extraindo uma coluna

```text
python3 -m dataset_io.cli datasets/validos/iris_amostra.csv --format csv --column petal_length --type float
```

### JSON de strings

```text
python3 -m dataset_io.cli datasets/validos/strings_numericas.json --format json --type text
```

### Entrada inválida com tipos misturados

```text
python3 -m dataset_io.cli datasets/invalidos/tipos_misturados.json --format json --type raw
```

Esse último comando deve terminar com erro de validação, pois a lista contém
inteiros e texto que não podem ser comparados diretamente.

## Limites deliberados

- O pacote não ordena valores.
- O pacote não recebe uma função `key` para ordenar registros completos.
- O pacote não decide como corrigir dados ausentes; ele os rejeita quando não
  são comparáveis.
- O pacote não prova que uma comparação personalizada é uma ordem total; ele
  apenas identifica incompatibilidades básicas.
