def merge(left: list[int], right: list[int]) -> list[int]:
  """
  Intercala dois vetores ordenados de forma iterativa.

  Args:    result = merge(left, right)

      left: Primeiro vetor ordenado.
      right: Segundo vetor ordenado.

  Returns:
      Um novo vetor contendo os elementos de left e right
      em ordem crescente.
  """

  result = []

  left_index = 0
  right_index = 0

  while left_index < len(left) and right_index < len(right):

    if left[left_index] <= right[right_index]:
      result.append(left[left_index])
      left_index += 1
    else:
      result.append(right[right_index])
      right_index += 1

  result.extend(left[left_index:])
  result.extend(right[right_index:])

  return result