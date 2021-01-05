# 주의할 점, 입력받은 x축은 가로 축을 나타냄 -> 열 임.
# 각 칸 순회 후 처음 배추가 발견된 지점에서 완전탐색
# 완전탐색은 dfs, bfs 등 상관 X
# dfs가 더 메모리 적게 소모, 재귀 시 깊이 지정

import sys
input = sys.stdin.readline
from collections import deque

for _ in range(int(input())):
    m, n, k = map(int, input().split())

    lis = [[0]*m for i in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        lis[y][x] = 1
    count = 0

    def dfs(lis, i, j):
        dx = [0,0,1,-1]
        dy = [1,-1,0,0] # 우, 좌, 하, 상
        stack = [[i,j]]
        
        while stack:
            a, b = stack.pop()
            lis[a][b] = -1
            for i in range(4):
                x = a + dx[i]
                y = b + dy[i]
                if 0 <= x < n and 0 <= y < m and lis[x][y] == 1:
                    lis[x][y] == -1
                    stack.append([x,y])

    
    for i in range(n):
        for j in range(m):
            if lis[i][j] <= 0:
                lis[i][j] = -1
            else:
                count += 1
                dfs(lis, i, j)

    print(count)

# i,j 순으로 순회하다가 1을 만나면 bfs 함수로 넘어가는데,
# bfs에서 이루어지는 순회를 -1해주어야 한다. 따라서 pop했을 때랑, 인접노드 스택에 넣어줄 때 -1 해주어야 함.

# 비슷한 문제 2667