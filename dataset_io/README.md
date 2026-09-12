# Camada de leitura e gerenciamento dos datasets

Esta camada prepara entradas para o Merge sort, mas não implementa nem chama a
ordenação. Ela lê arquivos, converte valores, valida as restrições e permite
consultar o catálogo de datasets.

## Componentes

| Componente | Responsabilidade |
| --- | --- |
| `readers.py` | Ler TXT, CSV e JSON e extrair valores brutos |
| `converters.py` | Converter texto, números e valores JSON |
| `validators.py` | Verificar comparabilidade e valores não finitos |
| `loader.py` | Orquestrar leitura, conversão, validação e metadados |
| `catalog.py` | Ler e validar o catálogo JSON versionado |
| `management.py` | Listar, inspecionar e validar entradas catalogadas |
| `formatters.py` | Produzir saída textual ou JSON |
| `cli.py` | Despachar o modo legado e os subcomandos de gerenciamento |
| `errors.py` | Padronizar mensagens de falha |

## Uso legado por caminho

Os comandos existentes continuam funcionando. Eles recebem diretamente um
arquivo e devolvem uma lista validada:

```bash
python3 -m dataset_io.cli \
  datasets/validos/iris_petal_length.txt \
  --format text \
  --type float
```

```bash
python3 -m dataset_io.cli \
  datasets/validos/iris_amostra.csv \
  --format csv \
  --column petal_length \
  --type float
```

## Gerenciamento pelo catálogo

O catálogo padrão está em `datasets/catalogo.json`. Os IDs seguem o catálogo
humano em `datasets/catalogo.md`:

```bash
python3 -m dataset_io.cli datasets list
```

O comando lista entradas locais, fixtures inválidas e fontes externas. Para
uma saída adequada a scripts:

```bash
python3 -m dataset_io.cli datasets list --output json
```

Para consultar uma entrada local:

```bash
python3 -m dataset_io.cli datasets inspect V01 --sample 5
```

Para consultar uma entrada externa, a CLI exibe os metadados sem fazer
download:

```bash
python3 -m dataset_io.cli datasets inspect E02
```

Para validar uma entrada local:

```bash
python3 -m dataset_io.cli datasets validate V01
```

O comando `inspect` é informativo: uma entrada inválida é reportada com
`Status observado: inválido` e o comando termina com sucesso. Já `validate`
retorna:

- `0` quando a entrada é válida;
- `1` quando a entrada viola as restrições;
- `2` quando o ID, catálogo, arquivo ou suporte local é inválido.

Também é possível indicar outro catálogo, antes ou depois do subcomando:

```bash
python3 -m dataset_io.cli datasets --catalog caminho/catalogo.json list
python3 -m dataset_io.cli datasets list --catalog caminho/catalogo.json
```

## Relação com SOLID

- **Responsabilidade única:** leitor, conversor, validador, catálogo, serviço
  e formatador têm tarefas distintas.
- **Aberto/fechado:** novos leitores e formatadores podem ser adicionados sem
  alterar o serviço de carregamento.
- **Substituição de Liskov:** qualquer leitor compatível com `RawDatasetReader`
  pode ser injetado no `DatasetLoader`.
- **Segregação de interfaces:** as interfaces são pequenas e específicas.
- **Inversão de dependência:** o carregador depende de abstrações de leitor,
  conversor e validador, não de um formato concreto.

## Testes

A partir da raiz do repositório:

```bash
python3 -m unittest discover -s tests -v
ruff check dataset_io tests
ruff format --check dataset_io tests
```

## Limites deliberados

- O pacote não ordena valores.
- O pacote não recebe uma função `key` para ordenar registros completos.
- O pacote não corrige dados ausentes automaticamente.
- O pacote não baixa datasets externos.
- O pacote não prova que uma comparação personalizada é uma ordem total; ele
  apenas identifica incompatibilidades básicas.
