## Enunciado

### Objetivo

O Seminário tem como propósito estudar e explicar um problema computacional pertencente à classe P. Cada grupo escolherá um problema, explicará sua complexidade, mostrará aplicações e implementará em Python um algoritmo que o resolve.

Ao final, cada estudante deverá ser capaz de descrever o problema em termos de instância, entrada, saída e restrições, justificar sua pertinência à classe P, relacionar o problema a situações reais e explicar o funcionamento do algoritmo implementado.


### Apresentação

Cada grupo terá 15 minutos para apresentar. Após a apresentação, o professor fará perguntas ao grupo e a estudantes individualmente sobre o problema e a solução implementada. A apresentação deve conter (no mínimo):

1. **Descrição do problema:** instâncias, entradas, saídas e restrições, com pelo menos um exemplo pequeno.
2. **Justificativa de tratabilidade:** por que o problema pertence à classe P. A justificativa deve indicar o que mede o tamanho da entrada e por que o número de passos do algoritmo é limitado por um polinômio nesse tamanho.
3. **Exemplos de aplicação:** situações reais em que o problema aparece.
4. **Algoritmo implementado:** ideia central, funcionamento passo a passo em um exemplo e relação com a implementação entregue.


## Desenvolvimento
### 1. Descrição do problema
- [ ] instâncias
- [ ] entradas
- [ ] saídas
- [ ] restrições, com pelo menos um exemplo pequeno.

#### Descrição
É um algoritmo de ordenação, que por meio da ideia de de divisão e conquista, divide uma estrutura em subconjuntos e aplica ordenação nos elementos previamente extraído das estruturas originais, e então é realizado a combinação dos itens em um conjunto final ordenado.

Além do merge sort dispomos de outros algoritmos famosos de ordenação como o conhecido bubble sort, select sort e insertion sort, cada um com suas formas de resolver um mesmo problema: ordenação de elementos de forma eficiente.


Comparações

| Algoritmo      | Melhor tempo | Tempo médio | Pior tempo  |     |
| -------------- | :----------: | :---------: | :---------: | --- |
| Merge sort     | O(n log₂ n)  | O(n log₂ n) | O(n log₂ n) |     |
| Quick sort     |  O(n log n)  | O(n log n)  |    O(n²)    |     |
| Bubble sort    |     O(n)     |    O(n²)    |    O(n²)    |     |
| Insertion sort |     O(n)     |    O(n²)    |    O(n²)    |     |
| Selection sort |    O(n²)     |    O(n²)    |    O(n²)    |     |

ex de funcionamento:
Nível 0:        8 elementos
               /          \
Nível 1:      4            4
             / \          / \
Nível 2:    2   2        2   2
           / \ / \      / \ / \
Nível 3:  1  1 1  1    1  1 1  1


como acontece a divisão do array ao meio:
8 > 4 > 2 > 1

Por isso o **log₂(** 8 **)** = 3

e então o **n**=8 seria a quantidade de elementos processadas a cada nivel
Nível 0 = 8 elementos
Nível 1 = 8 elementos
Nível 2 = 8 elementos
Nível 3 = 8 elementos

#### instâncias
#### entradas
#### saídas
#### restrições
Limitado a filtragem com base em apenas 1 valor


### Justificativa de tratabilidade
por que o problema pertence à classe P. A justificativa deve indicar o que mede o tamanho da entrada e por que o número de passos do algoritmo é limitado por um polinômio nesse tamanho.

### Exemplos de aplicação
situações reais em que o problema aparece.

### Algoritmo implementado

Implementações:
- Recursiva:
	A forma recursiva de implementação espelha uma definição matemática de divisão e conquista, onde ele divide um array pela metade de forma recursiva até chegar em apenas um elemento, e então combina os dois valores (de forma ordenada neste momento)

- Iterativa:
	trata o array como um elemento individual e usa loops iterativamente para combinar pares adjacentes em blocos ordenados maiores

ideia central, funcionamento passo a passo em um exemplo e relação com a implementação entregue.