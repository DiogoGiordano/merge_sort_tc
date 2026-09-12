# Datasets do Merge sort

Este diretório reúne somente dados, amostras e documentação para os testes do
seminário. Nenhum arquivo deste diretório implementa o algoritmo.

A camada de leitura independente está em [`../dataset_io/README.md`](../dataset_io/README.md).
Ela prepara listas sem importar ou executar o Merge sort.

## Contrato da implementação

A função atual recebe uma sequência finita de elementos que possam ser
comparados entre si. Para uma entrada válida, esperamos:

- uma saída em ordem não decrescente;
- o mesmo número de elementos da entrada;
- preservação de cada valor e de sua quantidade de ocorrências;
- nenhuma exceção durante as comparações.

Um dataset real não é enviado inteiro para a função. Primeiro escolhemos uma
coluna ou uma chave e produzimos uma lista unidimensional. Uma tabela com
dicionários, valores ausentes ou tipos misturados precisa ser transformada ou
classificada como fora do escopo da implementação atual.

## Estrutura

### `validos/`

- `iris_amostra.csv`: 15 registros reais do Iris, selecionados da fonte UCI;
- `iris_petal_length.txt`: a coluna numérica `petal_length` dos 15 registros;
- `iris_petal_length.expected.txt`: saída esperada para essa coluna;
- `iris_classes.txt`: a coluna textual `class` dos mesmos registros;
- `iris_classes.expected.txt`: saída esperada para a coluna textual;
- `strings_numericas.json`: strings comparáveis, mas que demonstram a diferença
  entre ordem lexicográfica e ordem numérica;
- `strings_numericas.expected.json`: saída esperada desse caso.

### `invalidos/`

- `tipos_misturados.json`: inteiros e strings na mesma lista;
- `registros_dicionario.json`: registros sem uma chave de ordenação escolhida;
- `valores_ausentes.json`: `null` misturado com números;
- `nan.txt`: valor `NaN`, que não obedece à ordem usual dos números reais;
- `numeros_complexos.txt`: números complexos, sem ordem natural.

Os arquivos inválidos não devem ser tratados como falhas do algoritmo. Eles
servem para demonstrar que as restrições da entrada precisam ser respeitadas.
Para os casos com `TypeError`, a mensagem esperada é uma falha de comparação.
Para `NaN`, a implementação pode executar, mas não há garantia de uma saída
corretamente ordenada enquanto não for definida uma política para esse valor.

## Fontes externas

O subconjunto do Iris foi retirado do arquivo oficial `iris.data` da UCI:

- página do dataset: <https://archive.ics.uci.edu/dataset/53/iris>;
- arquivo de dados: <https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data>.

Para uma avaliação maior, a fonte recomendada é o MovieLens 100K:

- página oficial: <https://grouplens.org/datasets/movielens/100k/>;
- arquivo e README: <https://files.grouplens.org/datasets/movielens/>.

No MovieLens, deve ser extraída uma coluna numérica, como `rating` ou
`timestamp`. A tabela completa não deve ser enviada diretamente à função.
Para que outra pessoa reproduza o resultado, é necessário registrar a versão,
a coluna e a data de acesso. O arquivo completo não foi copiado para este
repositório por ser desnecessário para a demonstração e por ser preferível
baixá-lo da fonte oficial.

## Como os colegas devem usar os arquivos

1. Selecionar um arquivo em `validos/`.
2. Usar a camada `dataset_io` para extrair a coluna, converter os valores e
   validar a entrada.
3. Entregar a lista retornada à versão do Merge sort escolhida pelo grupo.
4. Comparar a saída com o arquivo `.expected` correspondente ou com a
   especificação registrada no catálogo.
5. Repetir o procedimento com os arquivos em `invalidos/` e registrar a
   exceção ou a ausência de garantia, sem considerar isso uma saída válida.
6. Registrar também o tamanho da entrada e se a lista original foi preservada.

## Distinções importantes

- Lista vazia, lista unitária, lista ordenada, lista invertida e duplicatas são
  entradas válidas.
- Uma lista de strings é válida, mas a comparação é lexicográfica.
- Uma lista de dicionários não é comparável diretamente na implementação atual.
- Um dataset grande não é “impossível”; pode apenas ser inadequado para uma
  implementação em memória ou exigir ordenação externa.
- O teste de entradas inválidas documenta as restrições da função; não prova
  que o algoritmo seja incapaz de ordenar esses dados após adaptação.
