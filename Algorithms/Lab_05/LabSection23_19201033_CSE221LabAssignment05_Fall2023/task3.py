# -*- coding: utf-8 -*-
"""task3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15HAIdkL4KT9rGVR_IKpK3eWYrI8qLdz3
"""

def dfs(u, grph, vis, lst):
    vis[u] = 1

    for v in grph[u]:
        if vis[v]:
            continue
        dfs(v, grph, vis, lst)
    lst.append(u)


input3 = open("/content/input3.txt", 'r')
output3 = open("/content/output3.txt", 'w')

node, edge = map(int, input3.readline().split())

graph = [[] for i in range(node+1)]

t_graph = [[] for i in range(node+1)]

for i in range(edge):
    a,b = map(int, input3.readline().split())
    graph[a].append(b)
    t_graph[b].append(a)


visited = [0]*(node+1)
t_visited = [0]*(node+1)


node_sequence_on_ending = []

#Run DFS
for i in range(1, node+1):
    if visited[i] == 0:
        dfs(i, graph, visited, node_sequence_on_ending)
node_sequence_on_ending.reverse()

scc = []
for i in node_sequence_on_ending:
    if t_visited[i] == 0:
        dfs(i, t_graph, t_visited, scc)

        scc.sort()
        for j in scc:
            output3.write(f"{j} ")
        output3.write(f"\n")
        scc = []


input3.close()
output3.close()