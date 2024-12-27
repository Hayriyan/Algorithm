def bubble_sort(arr):
    """Bubble Sort Implementation"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def selection_sort(arr):
    """Selection Sort Implementation"""
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def insertion_sort(arr):
    """Insertion Sort Implementation"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr




if __name__ == "__main__":
    array = [64, 34, 25, 12, 22, 11, 90]
    print("Bubble Sort:", bubble_sort(array.copy()))
    print("Selection Sort:", selection_sort(array.copy()))
    print("Insertion Sort:", insertion_sort(array.copy()))

   