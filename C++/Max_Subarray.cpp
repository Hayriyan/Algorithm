
#include <iostream>
#include <vector>
#include <climits>
int NlogN(std::vector<int> &nums, int l, int r)
{
    if (l == r)
    {
        return nums[l] > 0 ? nums[l] : 0;
    }

    int m = l + (r - l) / 2;

    int left = NlogN(nums, l, m);
    int right = NlogN(nums, m + 1, r);

    int cross_sum = 0;
    int l_cross = INT_MIN, r_cross = INT_MIN;

    int temp_sum = 0;
    for (int i = m; i >= l; --i)
    {
        temp_sum += nums[i];
        l_cross = std::max(l_cross, temp_sum);
    }

    temp_sum = 0;
    for (int i = m + 1; i <= r; ++i)
    {
        temp_sum += nums[i];
        r_cross = std::max(r_cross, temp_sum);
    }

    cross_sum = l_cross + r_cross;

    return std::max({left, right, cross_sum});
}

int N(std::vector<int> &nums){
    int n = nums.size();
       int cur_sum = 0;
       int max_sum = INT_MIN;
       for(int i = 0; i < n; i++){
        cur_sum += nums[i];
        max_sum = std::max(cur_sum, max_sum);
        if(cur_sum < 0){
            cur_sum = 0;
        }
       }
       return max_sum;
}

