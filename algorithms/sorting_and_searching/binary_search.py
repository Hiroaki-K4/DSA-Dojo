def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


if __name__ == "__main__":
    sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]
    print("sorted list: ", sorted_list)
    target = 7
    print("target: {0}, result: {1}".format(target, binary_search(sorted_list, target)))
    print(
        "target: {0}, result: {1}".format(
            target,
            binary_search_recursive(sorted_list, target, 0, len(sorted_list) - 1),
        )
    )
