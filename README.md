# merge_sort_tc
Trabalho de teoria da computação perguntas a ser respondidas!


- o que é merge sort?
- como ele funciona?
- vantagens e desvantagens do merge sort?
- ele serve para que tipo de dados?
- que tipo de dado ele não ordena?
- entao qualquer dado que nao seja comparavel se torna um caso impossivel de ordenar?
- Temos que fazer simulações e iterativo e recursivo? qual a diferença entre eles?

# AULA 2
## "como especificar um problema"

- quais dados são recebidos? [entrada]
- qual resposta deve ser reproduzida? [saída]
- o que torna uma resposta válida? [restrições]
- como comparar respostas válidas? [objetivo]
- e quando não existe solução? [caso limite]

# Problema e instância
- problema: uma descrição de um conjunto de instâncias que compartilham características comuns.
- instância: um caso específico de um problema.

# decisão e otimização
- decisão: dado um problema, existe uma solução que satisfaça as restrições? envolve uma pergunta de sim ou não.
- otimização: dado um problema, qual é a melhor solução entre soluções validas?
- maximizazar: encontrar a solução que maximize uma função objetivo.
- minimizar: encontrar a solução que minimize uma função objetivo.

# quatro elementos relacionados
- problema: regra geral para todos os casos.
- instância: caso específico do problema.
- solução: resposta para uma instância do problema.
- algoritmo: procedimento para encontrar uma solução para uma instância do problema.

# Entrada e saída
- entrada: lista finita de dados que descrevem uma instância do problema.
- saída: lista finita de dados que descrevem uma solução para a instância do problema.

# Restrições devinem a validade de uma solução [regra obrigatória]
- a resposta precisa preservar todos os elementos da entrada.
- exemplo ordenação: não duplicar numeros e nem remover numeros da entrada. 
- validade nao garante melhor solução, apenas que a solução é aceitável.

# solução vailda não significa solução ótima
- valida: satisfaz as restrições do problema.
- ótima: é a melhor solução entre as soluções validas do problema.

# Aula 3 
## Solução e verificação de problemas computacionais
- distinguir (solução candidata, valida e otima)
- comparar (resolver, verificar)
- verificar (formato, restrições, valor)
- compreender (corretude do problema)

## Distinguir solução candidata, valida e ótima
- solução candidata: tem a estrutura pedida pelo problema, ela ainda presisa ser examinada
- solução válida: satisfaz as restrições do problema, mas não garante que seja a melhor solução.
- solução ótima: é a melhor solução entre as soluções válidas do problema.


## Verificar: formato, restrições e valor(verificar significa testar cada regra separadamente, uma falha torna uma a candidata inválida)
- formato: a solução candidata tem a estrutura pedida pelo problema?
- restrições: a solução candidata satisfaz as restrições do problema?
- valor: a solução candidata é a melhor solução entre as soluções válidas do problema?

    - Como verificar a validade:
    1) Confirmar o formato
        A resposta possui a estrutura esperada?
    2) Identificar as restrições
        Quais regras precisam ser cumpridas?
    3) Testar cada regra
        Mostrar cálculos ou fatos usados.
    4) Concluir diretamente
        A candidata é válida ou inválida?

- valida nao significa ótima
    - validade: cumpre o formato e restriçoes. “Esta solução é permitida?”
    - otimalidade: Esta solução é a melhor  entre as soluções válidas. "existe outra válida que seja melhor?"


## Comparar: resolver e verificar (a "melhor" depende do objetivo do problema, que pode ser maximizar ou minimizar)

    - maior beneficio: maximizar a função objetivo.
    - menor custo: minimizar a função objetivo.
    - menor tempo: minimizar a função objetivo.
    - menor distancia: minimizar a função objetivo.
solução invalida não pode ser ótima, mas uma solução válida pode não ser ótima.
- resolver: encontrar uma solução para uma instância do problema.
- verificar: determinar se uma solução candidata é válida ou ótima para uma instância do problema.

## Compreender: corretude do problema
a corretude exige duas obrigações:
    1) correção da resposta: ao terminar atende à especificação.
    2) término: encerra após um número finito de passos.
- corretude do problema: a solução candidata é válida ou ótima para uma instância do problema
