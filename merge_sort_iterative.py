import math

def merge(left, right, metrics):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        metrics["comparisons"] += 1

        if left[i] <= right[j]:
            result.append(left[i])
            metrics["movements"] += 1
            i += 1
        else:
            result.append(right[j])
            metrics["movements"] += 1
            j += 1

    while i < len(left):
        result.append(left[i])
        metrics["movements"] += 1
        i += 1

    while j < len(right):
        result.append(right[j])
        metrics["movements"] += 1
        j += 1

    return result


def merge_sort_iterative(arr):
    n = len(arr)

    metrics = {
        "comparisons": 0,
        "movements": 0
    }

    if n <= 1:
        return arr, metrics

    width = 1

    while width < n:
        for i in range(0, n, 2 * width):
            left = arr[i:i + width]
            right = arr[i + width:i + 2 * width]

            merged = merge(left, right, metrics)

            for j in range(len(merged)):
                arr[i + j] = merged[j]
                metrics["movements"] += 1

        width *= 2

    return arr, metrics


if __name__ == "__main__":
    arr = [8, 3, 5, 1, 4, 2]

    result, metrics = merge_sort_iterative(arr)

    print("Entrada:", [8, 3, 5, 1, 4, 2])
    print("Saída:", result)
    print("Comparações:", metrics["comparisons"])
    print("Movimentos:", metrics["movements"])

    print("Complexidade de tempo: O(n log n)")
    print("Complexidade de espaço: O(n)")
    print("Estável: Sim")

