# -*- coding: utf-8 -*-
"""Class Evaluation Task _1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QTJL4dlmNxiwlR333XY58zSGEUaxIMeK
"""

flag = 18
c = 1
while flag <= 63 :

    if c % 2 ==0:
        if flag == 63:

            print((flag*(-1)), end = '')
        else:
             print((flag*(-1)), end = ', ')

    else:
        if flag == 63:

            print(flag, end='')
        else:
            print(flag, end=', ')
    c +=1
    flag +=9