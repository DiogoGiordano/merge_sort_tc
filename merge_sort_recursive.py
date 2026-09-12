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


def merge_sort_recursive(arr, metrics=None):
    if metrics is None:
        metrics = {
            "comparisons": 0,
            "movements": 0
        }

    if len(arr) <= 1:
        return arr, metrics

    mid = len(arr) // 2

    left, metrics = merge_sort_recursive(arr[:mid], metrics)
    right, metrics = merge_sort_recursive(arr[mid:], metrics)

    result = merge(left, right, metrics)

    return result, metrics


if __name__ == "__main__":
    arr = [8, 3, 5, 1, 4, 2]

    result, metrics = merge_sort_recursive(arr)

    print("Entrada:", arr)
    print("Saída:", result)
    print("Comparações:", metrics["comparisons"])
    print("Movimentos:", metrics["movements"])
    print("Complexidade de tempo: O(n log n)")
    print("Complexidade de espaço: O(n)")
    print("Estável: Sim")