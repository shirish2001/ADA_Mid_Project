# -*- coding: utf-8 -*-
"""Heap Sort.ipynb

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

def heap_sort(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

sizes = [1000000, 800, 20000, 400000, 600000, 100000]
heap_sort_times = []

for size in sizes:
    input_data = generate_input(size)
    time_taken = time_sorting_algorithm(heap_sort, input_data)
    heap_sort_times.append(time_taken)
    print(f"Execution time for Heap Sort with input size {size}: {time_taken} seconds")

# Plotting
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.bar(range(len(sizes)), heap_sort_times, color='g', alpha=0.7)
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.title('Heap Sort Time Complexity')
plt.xticks(range(len(sizes)), sizes)
plt.grid(True)
plt.show()