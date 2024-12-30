#include <iostream>
#include <vector>

int lower_bound(const std::vector<int>& data, int target) {
    int l = 0, r = data.size();
    while (l < r) {
        int mid = l + (r - l) / 2;
        if (data[mid] < target) {
            l = mid + 1;
        } else {
            r = mid;
        }
    }
    return l;
}

int upper_bound(const std::vector<int>& data, int target) {
    int l = 0, r = data.size();
    while (l < r) {
        int mid = l + (r - l) / 2;
        if (data[mid] <= target) {
            l = mid + 1;
        } else {
            r = mid;
        }
    }
    return l;
}