# -*- coding: utf-8 -*-
"""task_55

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QTJL4dlmNxiwlR333XY58zSGEUaxIMeK
"""

# Write a python program to reverse a list

lst = [1,2,34,5,6,8,9,0]

lst_1 = []

for i in range(len(lst)-1,-1,-1):

    lst_1.append(lst[i])

print(lst_1)