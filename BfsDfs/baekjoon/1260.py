# 인접행렬

# def dfs(v):
#     print(v, end=' ')
#     visit[v] = 1
#     for i in range(1, n + 1):
#         if visit[i] == 0 and s[v][i] == 1:
#             dfs(i)

# def bfs(v):
#     queue = [v]
#     visit[v] = 0
#     while(queue):
#         v = queue[0]
#         print(v, end=' ')
#         del queue[0]
#         for i in range(1, n + 1):
#             if visit[i] == 1 and s[v][i] == 1:
#                 queue.append(i)
#                 visit[i] = 0

# n, m, v = map(int, input().split())
# s = [[0] * (n + 1) for i in range(n + 1)]
# visit = [0 for i in range(n + 1)]
# for i in range(m):
#     x, y = map(int, input().split())
#     s[x][y] = 1
#     s[y][x] = 1
    
# dfs(v)
# print()
# bfs(v)

# 인접 리스트
import sys
input = sys.stdin.readline
from collections import deque


def dfs(graph, v):
    visited = {}
    stack = [v]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.setdefault(n)
            stack += reversed(graph[n])
    return visited

def bfs(graph, v):
    visited = {}
    queue = deque([v])
    
    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.setdefault(n)
            queue += graph[n]
    return visited

n, m, v = map(int, input().split())

graph = {i:[] for i in range(1,n+1)}
for i in range(1, m+1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for key in graph:
    graph[key].sort()

print(' '.join(list(map(str,dfs(graph, v)))))
print(' '.join(list(map(str,bfs(graph, v)))))



'''
import sys
input = sys.stdin.readline
from collections import deque


def dfs(graph, v):
    visited = []
    stack = [v]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += reversed(graph[n])
    return visited

def bfs(graph, v):
    visited = []
    queue = deque([v])
    
    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph[n]
    return visited

n, m, v = map(int, input().split())

graph = {i:[] for i in range(1,n+1)}
for i in range(1, m+1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for key in graph:
    graph[key].sort()

print(' '.join(list(map(str,dfs(graph, v)))))
print(' '.join(list(map(str,bfs(graph, v)))))
'''