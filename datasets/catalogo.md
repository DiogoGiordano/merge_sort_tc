# Catálogo de entradas

Este catálogo define o que deve ser testado e como cada entrada deve ser
interpretada. Os arquivos são pequenos de propósito: o objetivo é permitir
reprodução e discussão na apresentação.

## Entradas válidas

| ID | Arquivo | Tipo | Tamanho | Regra | Saída esperada |
| --- | --- | --- | ---: | --- | --- |
| V01 | `validos/iris_petal_length.txt` | `float` | 15 | Ordenação crescente dos comprimentos de pétala | `validos/iris_petal_length.expected.txt` |
| V02 | `validos/iris_classes.txt` | `str` | 15 | Ordenação lexicográfica das classes | `validos/iris_classes.expected.txt` |
| V03 | `validos/strings_numericas.json` | `str` | 3 | Ordem lexicográfica, não numérica | `validos/strings_numericas.expected.json` |
| V04 | `data.py` | `int` | 30 instâncias | Casos de borda e combinações numéricas | Campo `saida_esperada` |

O arquivo `validos/iris_amostra.csv` é a fonte local das duas primeiras
instâncias do Iris. Ele não deve ser enviado diretamente ao Merge sort: o
cabeçalho e as colunas precisam ser interpretados antes.

## Entradas inválidas ou fora do escopo atual

| ID | Arquivo | Motivo | Comportamento esperado |
| --- | --- | --- | --- |
| I01 | `invalidos/tipos_misturados.json` | `int` e `str` não são comparáveis diretamente | `TypeError` durante a comparação |
| I02 | `invalidos/registros_dicionario.json` | Não foi escolhida uma chave de ordenação | `TypeError` ou necessidade de adaptação |
| I03 | `invalidos/valores_ausentes.json` | `None` não possui ordem numérica com `int` | `TypeError` durante a comparação |
| I04 | `invalidos/nan.txt` | `NaN` não forma uma ordem usual com os floats | Sem garantia de saída correta |
| I05 | `invalidos/numeros_complexos.txt` | Complexos não possuem ordem natural | `TypeError` durante a comparação |

## Datasets externos selecionados

| Dataset | Uso escolhido | Status no repositório | Decisão |
| --- | --- | --- | --- |
| UCI Iris | Uma coluna numérica e uma coluna textual | Há amostra local de 15 linhas | Usar na demonstração |
| MovieLens 100K | `rating` ou `timestamp` após extração | Fonte documentada, sem cópia integral | Usar somente se houver tempo para baixar e registrar a versão |
| NYC 311 | Datas, identificadores ou valores após limpeza | Apenas fonte documentada | Deixar como aplicação adicional, não como teste principal |
| IBGE população | Coluna de população convertida para inteiro | Apenas fonte documentada | Opcional |

Para o seminário, dois datasets reais são suficientes: Iris como exemplo pequeno
e MovieLens 100K como exemplo maior. Os casos inválidos devem ser pequenos e
controlados, pois foram criados para demonstrar as restrições da função.

## Critério de aprovação

Uma entrada válida passa quando:

1. o algoritmo termina sem exceção;
2. a saída é não decrescente;
3. a saída possui o mesmo tamanho da entrada;
4. a saída preserva as ocorrências dos elementos;
5. a saída coincide com o arquivo esperado ou com uma ordenação de referência.

Uma entrada inválida não precisa produzir uma saída. O resultado esperado é
registrar a razão pela qual a entrada não pertence ao domínio da implementação
atual, distinguindo isso de um erro lógico do algoritmo.

## Metadados mínimos para uma execução real

Registrar no relatório de teste:

- dataset e versão;
- URL da fonte;
- data de acesso;
- coluna ou chave utilizada;
- tamanho da amostra;
- conversões e tratamento de ausentes;
- implementação executada;
- saída ou erro observado;
- se a lista original foi preservada.
