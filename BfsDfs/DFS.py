def dfs(graph, start):
    visited = []
    stack = [start]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
    return visited

def dfs_paths(graph, start, end):
    result = []
    stack = [(start,[start])]

    while stack:
        n, path = stack.pop()
        if n == end:
            result.append(path)
        else:
            for m in graph[n] - set(path):
                stack.append((m, path+[m]))
    return result 

graph_list = {1: set([2,3]),
        2: set([1,4,5]),
        3: set([1]),
        4: set([2]),
        5: set([2])}

root_node = 1

print(dfs(graph_list, root_node))
print(dfs_paths(graph_list, 1, 5))