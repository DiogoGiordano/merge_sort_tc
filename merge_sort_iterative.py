from merge_sort_recursive import merge


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


my_list = [5, 1, 6, 7, 8, 2, 2]
new_list = merge_sort_iterative(my_list)
new_list.append(9)
print(new_list)
print(my_list)
