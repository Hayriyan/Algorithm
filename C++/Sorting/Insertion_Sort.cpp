#include <iostream>
#include <vector>
#include <chrono>


void insertionSort(std::vector<int> &arr)
{
    int n = arr.size();
    for (int i = 1; i < n; ++i)
    {
        int key = arr[i];
        int j = i - 1;

        while (j >= 0 && arr[j] > key)
        {
            arr[j + 1] = arr[j];
            --j;
        }
        arr[j + 1] = key;
    }
}

int main(int argc, char *argv[]) {
    std::vector<int> arr;
    for (int i = 1; i < argc; ++i) {
        arr.push_back(std::stoi(argv[i]));
    }

    auto start = std::chrono::high_resolution_clock::now();
    insertionSort(arr);
    auto stop = std::chrono::high_resolution_clock::now();


    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(stop - start);
    std::cout << duration.count() / 1000000.0 << std::endl;  
    return 0;
}
