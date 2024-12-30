def counting_sort(arr):
    count_map = {}

    for num in arr:
        if num in count_map:
            count_map[num] += 1
        else:
            count_map[num] = 1

    keys = []
    for key in count_map:
        keys.append(key)

    keys.sort()

    j = 0
    for key in keys:
        for _ in range(count_map[key]):
            arr[j] = key
            j += 1
