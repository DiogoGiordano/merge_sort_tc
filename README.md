# merge_sort_tc
Trabalho de teoria da computação

## Material de datasets

Os dados e as regras de seleção estão em [`datasets/README.md`](datasets/README.md).
O catálogo de entradas válidas, inválidas e externas está em
[`datasets/catalogo.md`](datasets/catalogo.md).

Os arquivos em `datasets/` são amostras e documentação; eles não substituem a
execução do algoritmo nem alteram os arquivos de implementação.

## Execução da camada de datasets

Para listar o catálogo:

```bash
python3 -m dataset_io.cli datasets list
```

Para inspecionar uma entrada válida:

```bash
python3 -m dataset_io.cli datasets inspect V01 --sample 5
```

Para validar uma entrada:

```bash
python3 -m dataset_io.cli datasets validate V01
```

Os comandos acima apenas leem e validam dados. A execução do Merge sort e a
comparação com as saídas esperadas continuam sendo responsabilidades da
integração do grupo.

Os testes automatizados da camada podem ser executados com:

```bash
python3 -m unittest discover -s tests -v
```
