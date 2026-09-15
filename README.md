# merge_sort_tc

Implementação do Merge Sort (recursivo e iterativo) em Python.

## Como rodar

```bash
python3 main.py --values 8 3 5 1 4 2 --metrics
```

### Instância de exemplo

```
Entrada:  [8, 3, 5, 1, 4, 2]
Saída esperada: [1, 2, 3, 4, 5, 8]
```

## Outros comandos

Versão iterativa:
```bash
python3 main.py --values 8 3 5 1 4 2 --metrics --type 2
```

Vetor aleatório:
```bash
python3 main.py --random 20 --metrics
```

Rodar todos os testes:
```bash
python3 test.py
```

Exemplo de saída:
```
=============================================
MERGE SORT RECURSIVO
=============================================
Teste 01: PASSOU | Comparações:   0 | Movimentos:   0
Teste 02: PASSOU | Comparações:   0 | Movimentos:   0
Teste 03: PASSOU | Comparações:   1 | Movimentos:   2
Teste 04: PASSOU | Comparações:   1 | Movimentos:   2
Teste 05: PASSOU | Comparações:   5 | Movimentos:  12
Teste 06: PASSOU | Comparações:   7 | Movimentos:  12
Teste 07: PASSOU | Comparações:   5 | Movimentos:   8
Teste 08: PASSOU | Comparações:   8 | Movimentos:  12
Teste 09: PASSOU | Comparações:   4 | Movimentos:   8
Teste 10: PASSOU | Comparações:   5 | Movimentos:   8
Teste 11: PASSOU | Comparações:   8 | Movimentos:  12
Teste 12: PASSOU | Comparações:   7 | Movimentos:  12
Teste 13: PASSOU | Comparações:   4 | Movimentos:   8
Teste 14: PASSOU | Comparações:   5 | Movimentos:   8
Teste 15: PASSOU | Comparações:   8 | Movimentos:  12
Teste 16: PASSOU | Comparações:   9 | Movimentos:  16
Teste 17: PASSOU | Comparações:   6 | Movimentos:  12
Teste 18: PASSOU | Comparações:   7 | Movimentos:  12
Teste 19: PASSOU | Comparações:   7 | Movimentos:  12
Teste 20: PASSOU | Comparações:  13 | Movimentos:  20
Teste 21: PASSOU | Comparações:   7 | Movimentos:  12
Teste 22: PASSOU | Comparações:  14 | Movimentos:  20
Teste 23: PASSOU | Comparações:  16 | Movimentos:  24
Teste 24: PASSOU | Comparações:  10 | Movimentos:  16
Teste 25: PASSOU | Comparações:  25 | Movimentos:  34
Teste 26: PASSOU | Comparações:  25 | Movimentos:  34
Teste 27: PASSOU | Comparações:  21 | Movimentos:  29
Teste 28: PASSOU | Comparações:   7 | Movimentos:  12
Teste 29: PASSOU | Comparações:  12 | Movimentos:  20
Teste 30: PASSOU | Comparações:  65 | Movimentos:  88
Resumo: 30 passou(aram), 0 falhou(aram) | Total comparações: 312 | Total movimentos: 477

=============================================
MERGE SORT ITERATIVO
=============================================
Teste 01: PASSOU | Comparações:   0 | Movimentos:   0
Teste 02: PASSOU | Comparações:   0 | Movimentos:   0
Teste 03: PASSOU | Comparações:   1 | Movimentos:   2
Teste 04: PASSOU | Comparações:   1 | Movimentos:   2
Teste 05: PASSOU | Comparações:   8 | Movimentos:  15
Teste 06: PASSOU | Comparações:   5 | Movimentos:  15
Teste 07: PASSOU | Comparações:   5 | Movimentos:   8
Teste 08: PASSOU | Comparações:   8 | Movimentos:  15
Teste 09: PASSOU | Comparações:   4 | Movimentos:   8
Teste 10: PASSOU | Comparações:   5 | Movimentos:   8
Teste 11: PASSOU | Comparações:   8 | Movimentos:  15
Teste 12: PASSOU | Comparações:   8 | Movimentos:  15
Teste 13: PASSOU | Comparações:   4 | Movimentos:   8
Teste 14: PASSOU | Comparações:   5 | Movimentos:   8
Teste 15: PASSOU | Comparações:   8 | Movimentos:  15
Teste 16: PASSOU | Comparações:   7 | Movimentos:  18
Teste 17: PASSOU | Comparações:   8 | Movimentos:  15
Teste 18: PASSOU | Comparações:   5 | Movimentos:  15
Teste 19: PASSOU | Comparações:   9 | Movimentos:  15
Teste 20: PASSOU | Comparações:  14 | Movimentos:  21
Teste 21: PASSOU | Comparações:   6 | Movimentos:  15
Teste 22: PASSOU | Comparações:  13 | Movimentos:  21
Teste 23: PASSOU | Comparações:  16 | Movimentos:  24
Teste 24: PASSOU | Comparações:  11 | Movimentos:  18
Teste 25: PASSOU | Comparações:  26 | Movimentos:  40
Teste 26: PASSOU | Comparações:  24 | Movimentos:  40
Teste 27: PASSOU | Comparações:  22 | Movimentos:  36
Teste 28: PASSOU | Comparações:   9 | Movimentos:  15
Teste 29: PASSOU | Comparações:  14 | Movimentos:  21
Teste 30: PASSOU | Comparações:  69 | Movimentos: 100
Resumo: 30 passou(aram), 0 falhou(aram) | Total comparações: 323 | Total movimentos: 548

Todos os testes passaram nos dois algoritmos!
```

Salvar log de execução:
```bash
python3 main.py --values 8 3 5 1 4 2 --metrics --log-level DEBUG --log-file logs/execucao.log
```

Ver todas as opções:
```bash
python3 main.py --help
```
