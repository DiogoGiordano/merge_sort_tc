from .merge_base import merge

def merge_sort_iterative(arr):
    n = len(arr)
    metrics = {"comparisons": 0, "movements": 0}

    if n <= 1:
        return arr, metrics

    width = 1
    while width < n:
        for i in range(0, n, 2 * width):
            left = arr[i:i + width]
            right = arr[i + width:i + 2 * width]
            merged = merge(left, right, metrics)
            arr[i:i + len(merged)] = merged
        width *= 2

    return arr, metrics