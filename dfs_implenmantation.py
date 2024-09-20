# -*- coding: utf-8 -*-
"""dfs implenmantation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1k66jx2wlklBPoChAdeWUy28MXp9j0ybW

dfs implenmantation
"""

def dfs(graph, start, path = []):
  stack = [start]
  while stack:
    vertex = stack.pop(0)
    if vertex not in path:
      path = path + [vertex]
      stack = graph[vertex] + stack
  return path

if __name__ == '__main__':

  graph = {'A':['B','C','D'],
           'B':['E'],
           'C':['F','G'],
           'D':['H'],
           'E':['I'],
           'F':['J'],
           'G':[],
           'H':[],
           'I':[],
           'J':[]}

  print('dfs: ', dfs(graph, 'A'))