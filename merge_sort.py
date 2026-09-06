def merge_sort(arr):
    """
    Recebe um array e retorna um novo array ordenado.
    """

    # Caso-base:
    # Um array vazio ou com apenas um elemento já está ordenado.
    if len(arr) <= 1:
        return arr.copy()

    # Encontra a posição central do array.
    meio = len(arr) // 2

    # Divide o array em duas partes.
    esquerda = arr[:meio]
    direita = arr[meio:]

    # Ordena cada metade recursivamente.
    esquerda_ordenada = merge_sort(esquerda)
    direita_ordenada = merge_sort(direita)

    # Junta as duas metades ordenadas.
    return intercalar(esquerda_ordenada, direita_ordenada)


def intercalar(esquerda, direita):
    """
    Junta dois arrays que já estão ordenados.
    """

    resultado = []

    # Índices usados para percorrer os dois arrays.
    i = 0
    j = 0

    # Compara os elementos das duas partes.
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    # Adiciona os elementos que sobraram na parte esquerda.
    resultado.extend(esquerda[i:])

    # Adiciona os elementos que sobraram na parte direita.
    resultado.extend(direita[j:])

    return resultado
