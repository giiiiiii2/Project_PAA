# Anggita Setiawati_F55123092
import random
import time
import matplotlib.pyplot as plt

def generate_array(n, max_value=160, seed=42):
    random.seed(seed)
    return [random.randint(1, max_value) for _ in range(n)]

def is_unique(array):
    return len(array) == len(set(array))

def measure_time(func, *args):
    start = time.perf_counter()
    func(*args)
    return time.perf_counter() - start

def main():
    ns = [100, 150, 200, 250, 300, 350, 400, 500]
    max_value = 160
    seed = 42

    worst_case_times = []
    average_case_times = []

    for n in ns:
        array = generate_array(n, max_value, seed)
        worst_case_array = [1] * n

        worst_case_times.append(measure_time(is_unique, worst_case_array))
        average_case_times.append(measure_time(is_unique, array))

        print(f"n = {n}, Worst: {worst_case_times[-1]:.10f} s, Avg: {average_case_times[-1]:.10f} s")

    plt.plot(ns, worst_case_times, 'ro-', label='Worst Case')
    plt.plot(ns, average_case_times, 'bs-', label='Average Case')
    plt.title('Performance: Worst vs Average Case')
    plt.xlabel('Array Size (n)')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
