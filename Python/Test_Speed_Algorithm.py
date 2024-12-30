import os
import subprocess
import numpy as np
import matplotlib.pyplot as plt


def compile_and_run_cpp(cpp_file, input_data):
    output_dir = "./C++/bin/"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    executable = os.path.join(output_dir, os.path.basename(cpp_file).replace('.cpp', ''))

    compile_command = f"g++ {cpp_file} -o {executable} -std=c++11"
    compile_process = subprocess.run(compile_command, shell=True, capture_output=True)

    if compile_process.returncode != 0:
        print(f"Error compiling {cpp_file}:\n{compile_process.stderr.decode().strip()}")
        return None

    input_args = ' '.join(map(str, input_data))
    run_command = f"{executable} {input_args}"
    run_process = subprocess.run(run_command, shell=True, capture_output=True)

    if run_process.returncode != 0:
        print(f"Error running {cpp_file}:\n{run_process.stderr.decode().strip()}")
        return None

    try:
        output = run_process.stdout.decode().strip()
        return float(output)
    except ValueError:
        print(f"Invalid output from {cpp_file}: {output}")
        return None


def generate_graph(input_sizes, insertion_sort_times, merge_sort_times):
    if not insertion_sort_times or not merge_sort_times:
        print("Error: No valid timing data available to generate the graph.")
        return

    plt.figure(figsize=(10, 6))
    plt.plot(input_sizes, insertion_sort_times, label="Insertion Sort", marker='o')
    plt.plot(input_sizes, merge_sort_times, label="Merge Sort", marker='s')
    plt.xlabel('Input Size')
    plt.ylabel('Time Taken (seconds)')
    plt.title('Insertion Sort vs Merge Sort Performance')
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    input_sizes = [100, 200, 300, 400, 500, 700, 900, 1000, 2000]
    insertion_sort_times = []
    merge_sort_times = []

    for size in input_sizes:
        print(f"Processing input size: {size}")
        input_data = np.random.randint(0, 1000, size).tolist()

        insertion_sort_time = compile_and_run_cpp('./C++/Sorting/Insertion_Sort.cpp', input_data)
        if insertion_sort_time is not None:
            insertion_sort_times.append(insertion_sort_time)
        else:
            print(f"Skipping input size {size} for Insertion Sort due to errors.")

        merge_sort_time = compile_and_run_cpp('./C++/Sorting/Merge_Sort.cpp', input_data)
        if merge_sort_time is not None:
            merge_sort_times.append(merge_sort_time)
        else:
            print(f"Skipping input size {size} for Merge Sort due to errors.")

    generate_graph(input_sizes, insertion_sort_times, merge_sort_times)


if __name__ == '__main__':
    main()
