def merge_sort_iterative(arr):
  n = len(arr)
  if n <= 1:
    return arr

  width = 1
  while width < n:
    for i in range(0, n, 2 * width):
      left = arr[i : i + width]
      right = arr[i + width : i + 2 * width]
      arr[i : i + len(left) + len(right)] = merge(left, right)
    width *= 2
  return arr
