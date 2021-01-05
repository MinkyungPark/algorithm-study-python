import sys
input = sys.stdin.readline
from collections import deque


def dfs(lis,n,m):
    dx = [0,0,0,1,-1]
    dy = [0,1,-1,0,0]
          #우,좌,하,상
    q = deque([[1,1]])
    visited = [[0]*(m+1) for _ in range(n+1)]
    visited[1][1] = 1

    while q:
        a,b = q.popleft()
        if a == n and b == m:
            print(visited[n][m])
            sys.exit()
        for i in range(1,5):
            x = a + dx[i]
            y = b + dy[i]
            if n >= x > 0 and m >= y > 0:
                if int(lis[x][y]) == 1 and visited[x][y] == 0:
                    visited[x][y] = visited[a][b] + 1
                    q.append([x,y])

n, m = map(int, input().split())

lis = [[0]*(m+1)]
for _ in range(n):
    tmp = [0] + list(input())[:m]
    lis.append(tmp)

dfs(lis, n, m)