from .merge_base import merge

def merge_sort_iterative(arr: list[int]) -> list[int]:
  """
  Ordena um vetor usando Merge Sort iterativo.

  Args:
      arr: Vetor que será ordenado.

  Returns:
      Vetor ordenado.
  """

  n = len(arr)

  if n <= 1:
    return arr

  width = 1

  while width < n:

    for i in range(0, n, 2 * width):

      left = arr[i:i + width]

      right = arr[i + width:i + 2 * width]

      merged = merge(left, right)

      arr[        i:i + len(merged)] = merged

    width *= 2

  return arr