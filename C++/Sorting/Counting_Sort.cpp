#include <iostream>
#include <vector>
void Counting_Sort(std::vector<int> arr){

    std::unordered_map<int, int> map;

    for (auto num : arr) {
        map[num]++;
    }

    std::vector<int> keys;
    for (auto num : map) {
        keys.push_back(num.first);
    }

    std::sort(keys.begin(), keys.end());

    int j = 0;
    for (auto key : keys) {
        for (int i = 0; i < map[key]; i++) {
            arr[j++] = key;
        }
    }


}