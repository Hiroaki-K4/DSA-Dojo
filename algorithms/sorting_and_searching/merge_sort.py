from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:  # Base case: a list with 0 or 1 elements is already sorted
        return arr

    # Split the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the two sorted halves
    return merge(left_half, right_half)


def merge(left: List[int], right: List[int]) -> List[int]:
    sorted_array = []
    i = j = 0

    # Compare elements from both halves and add the smaller one to the sorted array
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    # Add remaining elements from the left half
    while i < len(left):
        sorted_array.append(left[i])
        i += 1

    # Add remaining elements from the right half
    while j < len(right):
        sorted_array.append(right[j])
        j += 1

    return sorted_array


if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    sorted_arr = merge_sort(arr)
    print("Sorted array:", sorted_arr)
