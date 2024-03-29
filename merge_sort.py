# -*- coding: utf-8 -*-
"""Merge Sort.ipynb

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

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

sizes = [1000000, 800, 20000, 400000, 600000, 100000]
merge_sort_times = []

for size in sizes:
    input_data = generate_input(size)
    time_taken = time_sorting_algorithm(merge_sort, input_data)
    merge_sort_times.append(time_taken)
    print(f"Execution time for Merge Sort with input size {size}: {time_taken} seconds")

# Plotting
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.bar(range(len(sizes)), merge_sort_times, color='r', alpha=0.7)
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.title('Merge Sort Time Complexity')
plt.xticks(range(len(sizes)), sizes)
plt.grid(True)
plt.show()