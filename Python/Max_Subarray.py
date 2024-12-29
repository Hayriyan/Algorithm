def NlogN(nums, l, r):
    if l == r:
        return nums[l] if nums[l] > 0 else 0

    m = l + (r - l) // 2

    left = NlogN(nums, l, m)
    right = NlogN(nums, m + 1, r)

    cross_sum = 0
    l_cross = float('-inf')
    r_cross = float('-inf')

    temp_sum = 0
    for i in range(m, l - 1, -1):
        temp_sum += nums[i]
        l_cross = max(l_cross, temp_sum)

    temp_sum = 0
    for i in range(m + 1, r + 1):
        temp_sum += nums[i]
        r_cross = max(r_cross, temp_sum)

    cross_sum = l_cross + r_cross

    return max(left, right, cross_sum)


def N(nums):
    n = len(nums)
    cur_sum = 0
    max_sum = float('-inf')
    
    for i in range(n):
        cur_sum += nums[i]
        max_sum = max(cur_sum, max_sum)
        if cur_sum < 0:
            cur_sum = 0
    
    return max_sum
