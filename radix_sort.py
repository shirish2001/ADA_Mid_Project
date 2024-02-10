# -*- coding: utf-8 -*-
"""Radix Sort.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1k_l0DTTFH1d3sHXlfXJZnlcd-fx1D_mx
"""

import time
import random

def generate_input(size):
    return [random.randint(0, size*10) for _ in range(size)]

def time_sorting_algorithm(algorithm, input_data):
    start_time = time.time()
    algorithm(input_data)
    end_time = time.time()
    return end_time - start_time

def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]
    return arr

sizes = [1000000, 800, 20000, 400000, 600000, 100000]
radix_sort_times = []

for size in sizes:
    input_data = generate_input(size)
    time_taken = time_sorting_algorithm(radix_sort, input_data)
    radix_sort_times.append(time_taken)
    print(f"Execution time for Radix Sort with input size {size}: {time_taken} seconds")

# Plotting
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.bar(range(len(sizes)), radix_sort_times, color='c', alpha=0.7)
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.title('Radix Sort Time Complexity')
plt.xticks(range(len(sizes)), sizes)
plt.grid(True)
plt.show()