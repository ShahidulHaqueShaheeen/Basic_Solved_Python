# -*- coding: utf-8 -*-
"""task_73

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QTJL4dlmNxiwlR333XY58zSGEUaxIMeK
"""

# Assume a list with numbers from 1 to 10 and then convert it into a dictionary where the key would be the numbers of the list and the values would be the square of those numbers.


lst = list(range(1, 11))


'''
Using comprehension
dct = {num: num**2 for num in lst}

'''
dct = {}
for i in lst:

    dct[i] = i**2

print(dct)

