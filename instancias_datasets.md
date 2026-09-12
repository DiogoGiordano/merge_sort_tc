# Instâncias, entradas e aplicações do Merge sort

Documento de apoio para a preparação do seminário. O objetivo é formalizar o
problema de ordenação, distinguir instâncias de datasets, registrar casos
válidos e inválidos e relacionar o Merge sort a dados e sistemas reais.

## 1. Problema estudado

O problema recebe uma sequência finita de elementos comparáveis e deve produzir
uma sequência com os mesmos elementos em ordem não decrescente.

Podemos representar uma entrada por:

```text
A = [a₁, a₂, ..., aₙ]
```

A saída deve ser uma permutação de `A`, isto é, deve preservar cada elemento e
sua quantidade de ocorrências, mas reorganizá-los de modo que:

```text
b₁ ≤ b₂ ≤ ... ≤ bₙ
```

Exemplo:

```python
entrada = [4, 1, 3, 1]
saida = [1, 1, 3, 4]
```

## 2. Instância, entrada e dataset

O problema abstrato é “ordenar uma sequência”. Uma **instância** é uma entrada
concreta desse problema:

```python
[8, 3, 5, 1]
```

Para essa instância, a saída esperada é:

```python
[1, 3, 5, 8]
```

Um **dataset** é uma fonte que contém muitos registros. Ele não é uma única
instância de Merge sort até que se escolha um subconjunto, uma coluna e uma
regra de ordenação. Por exemplo:

```text
ratings.csv completo  → dataset
1000 valores da coluna rating → uma instância
```

## 3. Restrições e hipóteses

### 3.1 Restrições do problema

Uma entrada válida deve:

- ser uma sequência finita;
- possuir elementos comparáveis entre si;
- permitir uma ordem consistente, normalmente uma ordem total ou uma ordem de
  comparação equivalente;
- aceitar valores repetidos;
- poder estar vazia, ordenada, invertida ou desordenada.

A saída deve:

- estar em ordem não decrescente;
- conter exatamente os mesmos elementos da entrada;
- preservar as quantidades de elementos repetidos;
- não perder nem criar elementos.

Não há uma restrição de que os valores sejam positivos ou inteiros. Números
negativos, zeros, números reais e strings podem ser usados, desde que a
comparação escolhida seja consistente.

### 3.2 Hipóteses da implementação atual

As funções do repositório trabalham diretamente com listas que oferecem:

- `len`, para obter o tamanho;
- fatiamento, como `arr[:meio]`;
- comparação direta entre elementos;
- elementos cujo operador de comparação produz resultados coerentes.

A implementação não recebe registros representados diretamente como
dicionários. Para ordenar um CSV, é necessário fazer um pré-processamento e
extrair uma coluna ou transformar cada registro em uma estrutura comparável.

Por exemplo, para ordenar somente avaliações:

```python
[4.0, 2.5, 5.0, 3.5]
```

Para ordenar tuplas, a primeira posição pode ser usada como chave principal:

```python
[(2024, 10), (2022, 8), (2023, 9)]
```

Nesse caso, as tuplas são comparadas lexicograficamente: primeiro pela primeira
posição e, em caso de empate, pela próxima.

Se a saída precisar manter o registro completo enquanto a ordenação usa apenas
uma coluna, será necessário definir uma adaptação específica com uma chave de
ordenação. Isso não faz parte da função atual.

A versão recursiva preferida pelo grupo retorna uma nova lista. A versão
iterativa atual escreve os blocos ordenados de volta em `arr`, portanto modifica
a lista recebida, embora ainda utilize listas temporárias durante a
intercalação.

Observação sobre a versão efetivamente presente no repositório: o arquivo atual
`merge_sort_recursive.py` retorna `arr` diretamente quando `len(arr) <= 1` e usa
`<` na intercalação. A descrição de uma versão que retorna uma nova lista no
caso-base e usa `<=` corresponde à versão preferida/esperada pelo grupo e deve
ser alinhada ao código antes da apresentação.

## 4. Instâncias válidas e casos de borda

| Categoria | Entrada | Saída esperada | Observação |
| --- | --- | --- | --- |
| Vazia | `[]` | `[]` | Caso-base |
| Unitária | `[5]` | `[5]` | Caso-base |
| Dois elementos | `[2, 1]` | `[1, 2]` | Menor exemplo não trivial |
| Já ordenada | `[1, 2, 3, 4]` | `[1, 2, 3, 4]` | Ainda percorre a estrutura do Merge sort |
| Ordem inversa | `[4, 3, 2, 1]` | `[1, 2, 3, 4]` | Exige várias escolhas na intercalação |
| Repetições | `[4, 2, 4, 1, 2]` | `[1, 2, 2, 4, 4]` | Repetições são permitidas |
| Negativos | `[-3, 0, -1, 2]` | `[-3, -1, 0, 2]` | Não há exigência de valores positivos |
| Tamanho ímpar | `[9, 3, 7, 1, 5]` | `[1, 3, 5, 7, 9]` | Uma metade pode ficar maior |
| Todos iguais | `[7, 7, 7, 7]` | `[7, 7, 7, 7]` | Útil para testar empates |
| Parcialmente ordenada | `[1, 2, 5, 3, 4]` | `[1, 2, 3, 4, 5]` | Simula dados reais já parcialmente organizados |

Uma entrada como `[]` não é impossível: é um caso de borda válido. O caso-base
é importante justamente para tratar entradas pequenas sem novas divisões.

## 5. Entradas inválidas ou que exigem pré-processamento

“Entrada impossível” deve ser entendida como entrada inválida para as
restrições definidas, e não como uma lista difícil de ordenar. Toda lista finita
de elementos adequadamente comparáveis pode ser ordenada.

| Entrada | Problema | Tratamento possível |
| --- | --- | --- |
| `[1, "2", 3]` | Inteiros e strings não são comparáveis diretamente em Python 3 | Converter tudo para um tipo comum |
| `[None, 4, 2]` | `None` não possui ordem numérica com inteiros | Remover, imputar ou definir uma posição para ausentes |
| `["10", "2"]` | Strings são comparadas lexicograficamente, não numericamente | Converter para `[10, 2]` |
| `[{ "nome": "Ana" }, { "nome": "Bruno" }]` | Dicionários não possuem ordenação padrão entre si | Extrair `nome` ou outra chave |
| Datas inválidas | Não há chave temporal válida | Corrigir, descartar ou marcar o registro |
| Gerador infinito | Não é uma sequência finita e pode nunca terminar | Limitar a entrada ou rejeitá-la |
| Valores `NaN` | Comparações com `NaN` não formam uma ordem numérica usual | Definir uma política para `NaN` antes da ordenação |
| Arquivo com cabeçalho misturado aos dados | O cabeçalho não é um registro numérico | Remover o cabeçalho e interpretar as colunas |

Esses problemas são normalmente resolvidos durante a limpeza dos dados. O
Merge sort recebe a sequência já preparada.

## 6. Datasets pesquisados

### 6.1 MovieLens

O GroupLens disponibiliza conjuntos de avaliações coletadas pelo serviço
MovieLens. O arquivo `ratings.csv` possui registros com os campos:

```text
userId, movieId, rating, timestamp
```

A versão `ml-latest-small` possui mais de 100 mil avaliações e é adequada para
educação e desenvolvimento. O README informa também que as linhas estão
ordenadas primeiro por `userId` e, dentro de cada usuário, por `movieId`.

Possíveis instâncias:

```text
Coluna rating:
[4.0, 2.5, 5.0, 3.5, 4.0]

Coluna timestamp:
[1461234567, 1398765432, 1500000000]
```

Casos estudáveis:

- valores repetidos, porque várias avaliações podem ter a mesma nota;
- entrada parcialmente ordenada, pela organização original por usuário e filme;
- listas grandes obtidas selecionando milhares ou milhões de avaliações;
- ordenação de registros por nota, data ou identificador.

Para um experimento reprodutível, deve-se fixar uma versão do arquivo. O
GroupLens informa que os conjuntos “latest” são voltados a desenvolvimento e
podem mudar; a versão MovieLens 100K é uma alternativa de benchmark estável.

Fontes: [página do MovieLens no GroupLens](https://lenskit.grouplens.org/datasets/movielens/), [README do `ml-latest-small`](https://files.grouplens.org/datasets/movielens/ml-latest-small-README.html).

### 6.2 NYC 311 Service Requests

O portal oficial NYC Open Data disponibiliza solicitações de serviço feitas à
cidade de Nova York. A página consultada informa aproximadamente 22,3 milhões
de linhas, 44 colunas e atualização diária. Entre os campos estão `Unique Key`,
`Created Date`, `Closed Date`, agência, problema e localização.

Possíveis instâncias:

```text
Datas de criação:
["2024-03-10", "2024-01-02", "2024-03-10"]

Identificadores:
[512, 104, 987, 104]
```

Casos estudáveis:

- datas repetidas;
- registros abertos e fechados, que exigem política para datas ausentes;
- entradas muito grandes;
- ordenação cronológica de solicitações para um painel de atendimento.

O arquivo completo é grande demais para ser tratado como uma pequena instância
de demonstração. A recomendação é selecionar um período ou uma amostra e
registrar a data do download. O dataset é atualizado diariamente, então uma
execução futura pode encontrar dados diferentes.

Fonte: [NYC Open Data — 311 Service Requests](https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2020-to-Present/erm2-nwe9).

### 6.3 População dos municípios — IBGE

O IBGE disponibiliza tabelas oficiais com população dos municípios brasileiros e
arquivos para download em formatos como XLS e ODS. Esse material permite criar
uma instância brasileira extraindo a coluna de população e convertendo seus
valores para inteiros.

Exemplo conceitual:

```text
[158042, 6119, 63268, 38843]
→ [6119, 38843, 63268, 158042]
```

Casos estudáveis:

- valores de magnitudes diferentes;
- populações repetidas entre municípios;
- ordenação crescente ou decrescente;
- ordenação dos municípios por população, mantendo o nome como informação
  associada.

É importante interpretar corretamente separadores de milhares. Um valor como
`30.214` em uma tabela brasileira pode representar trinta mil duzentos e
quatorze, e não o número decimal `30.214`.

Fontes: [IBGE — população dos municípios](https://www.ibge.gov.br/estatisticas/sociais/populacao/37734-relacao-da-populacao-dos-municipios-para-publicacao-no-tcu.html), [IBGE — códigos dos municípios](https://www.ibge.gov.br/explica/codigos-dos-municipios.php).

### 6.4 Compras públicas do Governo Federal

O Portal Brasileiro de Dados Abertos disponibiliza conjuntos de compras públicas
com recursos em CSV e JSON. A página descreve registros de contratos, objetos,
vigências, órgãos e itens de contratação.

Possíveis instâncias:

```text
Valores de contratos:
[1200.50, 300.00, 1200.50, 75.90]

Códigos de órgãos:
["B", "A", "C", "A"]
```

Casos estudáveis:

- ordenação por valor, data, órgão ou código;
- valores repetidos;
- registros com campos ausentes;
- necessidade de converter valores monetários e datas antes da comparação.

Fonte: [Dados.gov.br — Compras públicas do Governo Federal](https://dados.gov.br/dados/conjuntos-dados/compras-publicas-do-governo-federal).

## 7. Como transformar um dataset em uma entrada do Merge sort

O fluxo recomendado é:

```text
arquivo bruto
    ↓
seleção de uma coluna ou chave
    ↓
limpeza e conversão dos valores
    ↓
lista finita de elementos comparáveis
    ↓
Merge sort
    ↓
saída ordenada
```

Exemplo com avaliações:

```text
ratings.csv
    ↓
selecionar rating
    ↓
converter para float
    ↓
[4.0, 2.5, 5.0, 3.5]
    ↓
[2.5, 3.5, 4.0, 5.0]
```

Ao apresentar um dataset, é importante registrar:

- endereço da fonte;
- versão ou data de acesso;
- coluna usada como chave;
- tratamento de valores ausentes;
- tamanho da amostra;
- saída esperada ou forma de validação.

Não é necessário colocar no repositório um dataset enorme. É melhor manter uma
pequena amostra reproduzível e documentar como obtê-la. Datasets dinâmicos,
como o NYC 311, devem ser identificados pelo período ou pela data de extração.

## 8. Sistema real relacionado

Um sistema de atendimento pode receber milhões de solicitações e precisar
produzir um relatório ordenado por data:

```text
solicitações recebidas
        ↓
separação em blocos menores
        ↓
ordenação de cada bloco
        ↓
arquivos temporários ordenados
        ↓
intercalação dos blocos
        ↓
relatório final ordenado
```

Quando todos os registros não cabem na memória, essa ideia é chamada de
**ordenação externa**. Ela mantém a mesma lógica central do Merge sort: ordenar
partes e depois intercalar partes já ordenadas.

O código-fonte do PostgreSQL contempla métodos de ordenação chamados `external
sort` e `external merge`. O comando GNU `sort` também oferece `--merge`, que
combina arquivos que já estão individualmente ordenados. Isso não significa que
toda ordenação de todo sistema use exatamente a implementação didática deste
repositório; o método pode variar conforme memória, índices e tipo de consulta.

Fontes: [código de ordenação do PostgreSQL](https://doxygen.postgresql.org/tuplesort_8c_source.html), [manual do GNU `sort`](https://www.gnu.org/software/coreutils/manual/html_node/The-sort-command.html).

## 9. Complexidade e classe P

Se `n` é o número de elementos, a versão recursiva satisfaz aproximadamente:

```text
T(n) = 2T(n/2) + Θ(n)
```

As duas chamadas processam metades da entrada e a intercalação custa `Θ(n)`.
Como existem aproximadamente `log₂(n)` níveis e cada nível processa `n`
elementos, temos:

```text
T(n) = Θ(n log n)
```

Isso vale para qualquer ordem inicial da lista: ordenada, invertida ou aleatória.
A estrutura das divisões depende do tamanho da entrada, não dos valores.

Na implementação recursiva:

```text
tempo: Θ(n log n)
espaço auxiliar: O(n)
pilha de recursão: O(log n)
```

Na implementação iterativa:

```text
tempo: Θ(n log n)
espaço temporário: O(n)
pilha de recursão: O(1)
```

No modelo usual de comparação, consideramos `n` como a quantidade de elementos
e cada comparação como uma operação de custo constante. Como:

```text
log₂(n) ≤ n
```

para `n ≥ 2`, segue que:

```text
n log₂(n) ≤ n²
```

Assim, `n log n` é limitado por um polinômio. Portanto, a ordenação por Merge
sort possui tempo polinomial e se enquadra na ideia de tratabilidade exigida
pelo seminário.

## 10. Mensagem central para a apresentação

> “Uma instância do Merge sort é uma sequência finita de elementos comparáveis.
> A saída deve conter os mesmos elementos em ordem não decrescente. Datasets
> reais fornecem muitas instâncias possíveis, mas precisam ser limpos e
> transformados em valores ou registros comparáveis. O Merge sort divide a
> entrada, ordena as partes e as intercala em `Θ(n log n)`. Como esse tempo é
> limitado por um polinômio, o problema é tratável em tempo polinomial."

## 11. Artefatos locais para os testes

As amostras e o catálogo de decisões foram separados deste documento:

- [`datasets/README.md`](datasets/README.md): instruções e regras de uso;
- [`datasets/catalogo.md`](datasets/catalogo.md): entradas, fontes, tamanhos e
  critérios de aprovação;
- [`datasets/validos/`](datasets/validos/): entradas válidas e saídas esperadas;
- [`datasets/invalidos/`](datasets/invalidos/): entradas inválidas ou fora do
  escopo da implementação atual.

As amostras locais do Iris são pequenas e reproduzíveis. O MovieLens 100K ficou
registrado como fonte externa para um teste maior; caso seja utilizado, a equipe
deve registrar a versão, a coluna extraída, a data de acesso e o resultado da
execução, sem afirmar que o dataset foi testado antes disso.

## 12. Gerenciamento pela CLI

O catálogo estruturado está em [`datasets/catalogo.json`](datasets/catalogo.json)
e pode ser consultado sem executar o Merge sort:

```bash
python3 -m dataset_io.cli datasets list
python3 -m dataset_io.cli datasets inspect V01 --sample 5
python3 -m dataset_io.cli datasets validate V01
```

`list` reúne entradas válidas, inválidas e externas. `inspect` mostra metadados
e uma amostra. `validate` verifica se uma entrada local satisfaz as restrições;
ele retorna código `0` para entrada válida, `1` para entrada inválida e `2`
quando o dataset não pode ser validado localmente. Fontes externas são apenas
catalogadas e não são baixadas pela CLI.
