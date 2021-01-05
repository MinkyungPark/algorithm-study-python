import sys
input = sys.stdin.readline

n = int(input())
lis = []

for _ in range(n):
    tmp = []
    for t in list(map(str, input().strip())):
        tmp.append(int(t))
    lis.append(tmp)

def dfs(lis, i, j):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    stack = [[i,j]]
    result.setdefault(count,[[i,j]])

    while stack:
        a, b = stack.pop()
        lis[a][b] = -1
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < n and lis[x][y] == 1:
                result[count].append([x,y])
                lis[x][y] = -1
                stack.append([x,y])


count = 0
result = {}

for i in range(n):
    for j in range(n):
        if lis[i][j] == 0:
            lis[i][j] = -1
        if lis[i][j] == 1:
            count += 1
            dfs(lis, i, j)

print(len(result))
total = []
for key in result:
    total.append(len(result[key]))

total.sort()
for t in total:
    print(t)