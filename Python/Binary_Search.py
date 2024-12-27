def binary_search(arr, target):
    """Binary Search Implementation"""
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  


if __name__ == "__main__":
    sorted_array = [11, 12, 22, 25, 34, 64, 90]
    target = 25
    index = binary_search(sorted_array, target)
    if index != -1:
        print(f"Element {target} found at index {index}.")
    else:
        print(f"Element {target} not found.")
