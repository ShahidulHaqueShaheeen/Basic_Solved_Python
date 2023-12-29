# -*- coding: utf-8 -*-
"""Task-3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15HAIdkL4KT9rGVR_IKpK3eWYrI8qLdz3
"""

#Task-3

input_3 = open('/content/input4.txt', 'r')
output_3 = open('/content/output4.txt','w')

data = input_3.readlines()

n = int(data[0])
id_li = data[1].split(" ")
mark_li = data[2].split(" ")


for i in range(n-1, -1, -1):    # Selection Sort
  for j in range(0, i+1):
    if(j==0):
      mark_min=int(mark_li[j])
      mark_min_idx=j
    if(int(mark_li[j]) == mark_min):
      if(int(id_li[j]) > int(id_li[mark_min_idx])):
        mark_min = int(mark_li[j])
        mark_min_idx = j
    elif(int(mark_li[j]) < mark_min):
      mark_min = int(mark_li[j])
      mark_min_idx = j


  mark_li[mark_min_idx], mark_li[j] = mark_li[j], mark_li[mark_min_idx]
  id_li[mark_min_idx], id_li[j] = id_li[j], id_li[mark_min_idx]

#print(mark_li)
#print(id_li)

for a in range(n):
  output_3.write(f"ID: {int(id_li[a])} Mark: {int(mark_li[a])} \n")

input_3.close()
output_3.close()