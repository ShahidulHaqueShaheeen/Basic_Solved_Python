# -*- coding: utf-8 -*-
"""Home Task _4

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QTJL4dlmNxiwlR333XY58zSGEUaxIMeK
"""

q = int(input())

inputs = []

for i in range(q):
    temp = int(input())
    inputs.append(temp)
#print(inputs)
max = inputs[0]
min = inputs[0]
sum = inputs[0]
for i in range(1,len(inputs)):

    sum += inputs[i]

    if inputs[i] > max:
        max = inputs[i]
    if inputs[i] < min:
        min = inputs[i]
avg = sum/q
print(f"Maximum {max}")
print(f"Minimum {min}")
print(f"Average is {avg}")