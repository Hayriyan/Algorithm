def bubble_sort(arr):
    """Bubble Sort Implementation"""
    n = len(arr)
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def selection_sort(arr):
    """Selection Sort Implementation"""
    n = len(arr)
    for i in range(n):
        # Find the minimum element in the remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def insertion_sort(arr):
    """Insertion Sort Implementation"""
    for i in range(1, len(arr)):
        # Extract the current element to be inserted
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def binary_search(arr, target):
    """Binary Search Implementation"""
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # Target not found


# Example Usage
if __name__ == "__main__":
    # Sorting examples
    array = [64, 34, 25, 12, 22, 11, 90]
    print("Bubble Sort:", bubble_sort(array.copy()))
    print("Selection Sort:", selection_sort(array.copy()))
    print("Insertion Sort:", insertion_sort(array.copy()))

    # Binary Search example
    sorted_array = [11, 12, 22, 25, 34, 64, 90]
    target = 25
    index = binary_search(sorted_array, target)
    if index != -1:
        print(f"Element {target} found at index {index}.")
    else:
        print(f"Element {target} not found.")
