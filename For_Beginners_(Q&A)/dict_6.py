# -*- coding: utf-8 -*-
"""dict_6

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QTJL4dlmNxiwlR333XY58zSGEUaxIMeK
"""

student_dict = {
    'Student1': [85, 90, 78, 92, 88],
    'Student2': [76, 88, 95, 80, 87],
    'Student3': [90, 82, 79, 88, 91],
    'Student4': [85, 89, 93, 87, 80],
    'Student5': [78, 91, 85, 89, 84],
}

for k , v in student_dict.items():

    print(f"{k} has scored total {sum(v)} marks and percentage of it is about {sum(v) / 500 *100 : .2f}")
    total = 0
    for i in v:
        total += i
    p = total / 500 *100
    print(print(f"{k} has scored total {total} marks and percentage of it is about {p : .2f}"))

student_dict = {
    'Student1': [85, 90, 78, 92, 88],
    'Student2': [76, 88, 95, 80, 87],
    'Student3': [90, 82, 79, 88, 91],
    'Student4': [85, 89, 93, 87, 80],
    'Student5': [78, 91, 85, 89, 84],
}

for k , v in student_dict.items():

    print(f"{k} has scored total {sum(v)} marks and percentage of it is about {sum(v) / 500 *100 : .2f}")
    total = 0
    for i in v:
        total += i
    p = total / 500 *100
    print(print(f"{k} has scored total {total} marks and percentage of it is about {p : .2f}"))

student_dict = {
    'Student1': [85, 90, 78, 92, 88],
    'Student2': [76, 88, 95, 80, 87],
    'Student3': [90, 82, 79, 88, 91],
    'Student4': [85, 89, 93, 87, 80],
    'Student5': [78, 91, 85, 89, 84],
}

for k, v in student_dict.items():
    print(f"{k} has scored total {sum(v)} marks and percentage of it is about {sum(v) / 500 *100 : .2f}")
    total = 0
    for i in v:
        total += i
    p = total / 500 * 100
    print(f"{k} has scored total {total} marks and percentage of it is about {p : .2f}")