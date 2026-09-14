# Merge Sort — Teoria da Computação (AL0349/AL0501)

Seminário sobre um problema pertencente à classe **P**. Tema do grupo: **problema da ordenação, resolvido pelo algoritmo Merge Sort**.

> Disciplina: Teoria da Computação — Prof. Dr. Paulo Silas Severo de Souza (paulosilas@unipampa.edu.br)

---

## Sumário

1. [Descrição do problema](#1-descrição-do-problema)
2. [Justificativa de tratabilidade (por que está em P)](#2-justificativa-de-tratabilidade-por-que-está-em-p)
3. [Exemplos de aplicação](#3-exemplos-de-aplicação)
4. [Algoritmo implementado](#4-algoritmo-implementado)
5. [Implementação](#5-implementação)
---

## 1. Descrição do problema

Seguindo o roteiro de especificação da Aula 02 (entrada, saída, restrições, objetivo, caso-limite):

### Problema (regra geral)

> Dada uma sequência finita de elementos sobre os quais existe uma relação de ordem total, produzir uma sequência contendo os mesmos elementos, reorganizados em ordem não decrescente.

### Instância (caso concreto)

Uma instância é uma sequência específica de valores. Exemplo: `A = [8, 3, 5, 1]`.

### Entrada

- Uma lista finita de `n` elementos comparáveis entre si (ou seja, existe uma relação `≤` definida para qualquer par de elementos da lista).
- `n` pode ser qualquer inteiro não negativo (`n ≥ 0`).

### Saída

- Uma lista de `n` elementos, contendo exatamente os mesmos elementos da entrada, reorganizados de forma que `saída[i] ≤ saída[i+1]` para todo `i` de `0` até `n-2`.

### Restrições (o que torna uma saída válida)

1. **Preservação (permutação):** a saída deve ser uma permutação exata da entrada — mesma quantidade de elementos, sem adicionar, remover ou duplicar nenhum valor.
2. **Ordem:** todo elemento na posição `i` deve ser menor ou igual ao elemento na posição `i+1`.
3. **Comparabilidade:** os elementos precisam ter uma relação de ordem bem definida (números, strings em ordem alfabética, datas, ou objetos com um critério de comparação explícito).
4. **Estabilidade (opcional/desejável):** elementos com o mesmo valor devem manter a ordem relativa original — o Merge Sort, implementado corretamente, garante essa propriedade, o que o diferencia de algoritmos como quicksort e selection sort.

> ⚠️ Para o Merge Sort, a restrição relevante é a comparabilidade dos elementos — não é necessário que sejam números, mas eles precisam ser comparáveis entre si. Por exemplo, uma lista de strings ou uma lista de objetos com um método de comparação definido são entradas válidas.

### Caso-limite

- Lista vazia (`n = 0`) → saída é a lista vazia.
- Lista com um único elemento (`n = 1`) → já está ordenada, nenhuma operação necessária.
- Lista com elementos sem relação de ordem definida → o problema **não está definido** para essa entrada (ver Exemplo 2).

### Exemplo pequeno 1 — entrada válida

```
Entrada:  [8, 3, 5, 1]
Saída:    [1, 3, 5, 8]
```

### Exemplo pequeno 2 — caso-limite de comparabilidade

```
Entrada:  [3, "gato", 7]
```
Não é uma instância válida do problema: não existe uma relação de ordem natural entre um número e uma string nesse contexto, então "ordenar" não está definido. Isso mostra que a restrição de comparabilidade não é decorativa — ela delimita exatamente quais entradas o problema aceita.

---

## 2. Justificativa de tratabilidade (por que está em P)

### O que mede o tamanho da entrada (n)

`n` = número de elementos da lista de entrada. Não é o valor dos elementos, nem o número de bits necessários para representá-los — é a **quantidade de itens a ordenar**.

### Por que o número de passos é limitado por um polinômio em n

O Merge Sort segue a estratégia de **divisão e conquista**:

1. **Dividir:** a lista é dividida ao meio recursivamente até restarem sublistas de 1 elemento (que já estão trivialmente ordenadas). Como a divisão é sempre pela metade, a profundidade da recursão é `log₂ n`.
2. **Combinar (merge):** juntar duas sublistas já ordenadas de tamanho total `k` custa no máximo `k - 1` comparações — ou seja, custo **linear** em relação ao tamanho combinado.
3. Em cada um dos `log₂ n` níveis da recursão, a soma dos tamanhos das sublistas processadas é sempre `n` (todos os elementos são tocados uma vez por nível), então cada nível custa `O(n)`.

Isso dá a recorrência clássica:

```
T(n) = 2·T(n/2) + O(n)
```

Que resolve para:

```
T(n) = Θ(n log₂ n)
```

### Por que isso é polinomial

`n log₂ n` cresce mais devagar que `n²` para qualquer `n` (a partir de valores pequenos), e `n²` já é um polinômio de grau fixo (`k = 2`). Como `T(n) ∈ O(n²)`, o Merge Sort satisfaz a definição de P vista na Aula 04: **existe um algoritmo determinístico cujo número de passos é limitado por `nᵏ`, com `k` fixo** (aqui, de forma ainda mais forte, por `n log n`, que é mais restrito que qualquer polinômio de grau ≥ 1 + ε).

### Ponto forte para a arguição: melhor, médio e pior caso coincidem (Θ, não só O)

Ao contrário de algoritmos como Quick Sort (pior caso `O(n²)`) ou Insertion Sort (melhor caso `O(n)`, pior caso `O(n²)`), o Merge Sort tem **o mesmo comportamento assintótico em todos os cenários**:

| Cenário | Complexidade |
|---|---|
| Melhor caso | Θ(n log n) |
| Caso médio | Θ(n log n) |
| Pior caso | Θ(n log n) |

Isso acontece porque a divisão ao meio e a estrutura do merge não dependem da ordem dos dados de entrada — o algoritmo sempre faz o mesmo número (assintótico) de comparações, independentemente de a lista já estar ordenada, invertida ou aleatória. Na linguagem da Aula 04: **o piso (Ω) e o teto (O) crescem no mesmo ritmo**, por isso é correto usar **Θ(n log n)**, e não apenas O(n log n).

### Comparação com outros algoritmos de ordenação (para contextualizar)

| Algoritmo | Melhor caso | Caso médio | Pior caso | Estável? | In-place? |
|---|---|---|---|---|---|
| **Merge Sort** | Θ(n log n) | Θ(n log n) | Θ(n log n) | Sim | Não (O(n) extra) |
| Quick Sort | Θ(n log n) | Θ(n log n) | Θ(n²) | Não | Sim |
| Bubble Sort | Θ(n) | Θ(n²) | Θ(n²) | Sim | Sim |
| Insertion Sort | Θ(n) | Θ(n²) | Θ(n²) | Sim | Sim |
| Selection Sort | Θ(n²) | Θ(n²) | Θ(n²) | Não | Sim |

---

## 3. Exemplos de aplicação

- **Ordenação externa (external sorting):** quando os dados não cabem inteiramente na memória RAM (ex.: arquivos de log gigantes, bancos de dados), o Merge Sort é a base dos algoritmos usados, pois processa blocos e faz merge sem precisar acessar tudo simultaneamente.
- **Bibliotecas padrão de linguagens:** o **Timsort**, usado por padrão em Python (`sorted()`, `.sort()`) e no Java, é um híbrido entre Merge Sort e Insertion Sort — a espinha dorsal continua sendo o merge.
- **Ordenação de listas encadeadas:** Merge Sort não depende de acesso aleatório a índices (diferente do Quick Sort, que se beneficia de acesso direto), o que o torna preferível para estruturas como listas ligadas.
- **Processamento distribuído/paralelo:** a etapa de "dividir" se paraleliza naturalmente (cada máquina ordena uma parte), e o "merge" final combina os resultados — é a base conceitual do padrão MapReduce aplicado à ordenação de grandes volumes de dados.
- **Ordenação estável necessária:** quando é preciso ordenar por múltiplos critérios preservando a ordem original em caso de empate (ex.: ordenar transações bancárias por valor, mantendo a ordem cronológica entre valores iguais).

---

## 4. Algoritmo implementado

### Ideia central

Divisão e conquista: **dividir** o problema em subproblemas menores do mesmo tipo, **resolver** cada subproblema recursivamente (ou trivialmente, no caso base), e **combinar** as soluções dos subproblemas em uma solução do problema original.

### Passo a passo com exemplo (versão recursiva)

Entrada: `[8, 3, 5, 1]`

**Divisão (top-down):**
```
Nível 0:        [8, 3, 5, 1]
Nível 1:    [8, 3]      [5, 1]
Nível 2:  [8]  [3]    [5]  [1]
```
A lista de 4 elementos leva `log₂ 4 = 2` níveis de divisão até chegar a sublistas de 1 elemento (caso base, já trivialmente ordenado).

**Combinação (merge, bottom-up):**
```
Nível 2 → 1:  [8] + [3] → [3, 8]        [5] + [1] → [1, 5]
Nível 1 → 0:  [3, 8] + [1, 5] → [1, 3, 5, 8]
```
No merge de `[3, 8]` com `[1, 5]`: compara-se `3` vs `1` (1 é menor, vai primeiro), depois `3` vs `5` (3 é menor), depois `8` vs `5` (5 é menor), e por fim só resta `8`. Resultado: `[1, 3, 5, 8]`.

### Implementação recursiva (top-down)

Espelha diretamente a definição matemática de divisão e conquista: a função chama a si mesma em cada metade até o caso base (lista de 0 ou 1 elemento), e então combina os resultados com a função de merge.

### Implementação iterativa (bottom-up)

Trata a lista inicial como `n` sublistas de tamanho 1 e vai fazendo merge de pares adjacentes em blocos progressivamente maiores (tamanho 1 → 2 → 4 → 8 ...), sem usar recursão/pilha de chamadas.

### Recursivo vs. iterativo — diferença prática

| Aspecto | Recursivo | Iterativo |
|---|---|---|
| Direção | Top-down (divide primeiro, combina depois) | Bottom-up (combina progressivamente) |
| Uso de memória | Pilha de chamadas (`O(log n)` de profundidade) | Sem pilha de recursão, mas pode usar buffers auxiliares |
| Clareza | Mais próxima da definição matemática | Mais próxima da execução real da máquina |
| Complexidade assintótica | Θ(n log n) — igual | Θ(n log n) — igual |



### Relação com a implementação entregue

O código em `mergesort.py` implementa a versão **[recursiva/iterativa — completar conforme o que o grupo decidir entregar]**, com duas funções centrais:

- `resolver(lista)`: constrói a solução ordenada (o algoritmo em si).
- `verificar(entrada, saida)`: função auxiliar que testa se a saída é uma solução **válida** — confirma que é permutação da entrada e que está em ordem não decrescente. Essa separação reflete diretamente a distinção entre **resolver e verificar** trabalhada na Aula 03: resolver constrói, verificar apenas examina.

### Corretude (Aula 03 — término + correção da resposta)

- **Término:** a cada chamada recursiva, o tamanho da sublista é reduzido pela metade; como o tamanho é um inteiro positivo decrescente, o processo necessariamente atinge o caso base (`n ≤ 1`) em um número finito de passos.
- **Correção (invariante):** o invariante mantido em cada chamada é *"a sublista retornada por cada chamada recursiva está ordenada"*. Isso é a base do caso indutivo: se as duas metades retornadas já estão ordenadas (hipótese de indução), o passo de merge combina duas listas ordenadas em uma lista ordenada maior — preservando o invariante até a chamada de nível mais alto, cuja saída é a lista completa ordenada.

---

## 5. Implementação

- **Linguagem:** Python 3.
- **Arquivo principal:** `mergesort.py` (ou `src/mergesort.py`).
- **Como executar:**
  ```bash
  python mergesort.py
  ```
- **Instância de exemplo incluída:**
  ```
  Entrada:  [8, 3, 5, 1]
  Saída esperada: [1, 3, 5, 8]
  ```
- **Repositório GitHub:** 

---

