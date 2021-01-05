from collections import deque

# dequeue 이용
def bfs_dequeue(graph, start):
    visited = []
    queue = deque([start])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
    return visited

# .pop(0) 이용
def bfs(graph, start):
    visited = []
    queue = [start]

    while queue:
        n = queue.pop(0)
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
    return visited

# 두 노드간 모든 경로 탐색
def bfs_paths(graph, start, end):
    queue = [(start, [start])]
    result = []

    while queue:
        n, path = queue.pop(0)
        if n == end:
            result.append(path)
        else:
            for m in graph[n] - set(path):
                queue.append((m, path+[m]))
    return result

# 방향이 있는 그래프
# graph_list = {1: set([3, 4]),
#               2: set([3, 4, 5]),
#               3: set([1, 5]),
#               4: set([1]),
#               5: set([2, 6]),
#               6: set([3, 5])}

# 방향X 그래프
graph_list = {1: set([2,3]),
        2: set([1,4,5]),
        3: set([1]),
        4: set([2]),
        5: set([2])}

root_node = 1
print(bfs(graph_list, root_node))
print(bfs_dequeue(graph_list, root_node))
print(bfs_paths(graph_list, 1, 5))