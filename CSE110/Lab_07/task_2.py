# -*- coding: utf-8 -*-
"""task_2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QTJL4dlmNxiwlR333XY58zSGEUaxIMeK
"""

import numpy as np

N = int(input("Enter the length of the the array : "))

arr = np.arange(N)

for i in range(N):
    arr[i] = int(input())
print(f"Original Array: {arr}")


for i in range(N):

    if arr[i] > 0:
        arr [i] = 1
    else:
        arr[i] = 0
print(f"After modifying: {arr}")

print(np.arange(3))