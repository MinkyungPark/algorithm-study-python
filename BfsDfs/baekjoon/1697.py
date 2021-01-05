# 경우의수, 완전탐색 - 브루트포스, 비트마스크, 순열(o(n)), 백트래킹, BFS로 풀 수 있음
#  N(0 ≤ N ≤ 100,000), K(0 ≤ K ≤ 100,000)
import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())

max = 100001
visited = [-1]*max
visited[n] = 0

q = deque([n])

while q:
    cur = q.popleft()
    if cur == k:
        print(visited[cur])
        sys.exit()

    for adj in [cur*2, cur+1, cur-1]:
        if 0 <= adj < max and visited[adj] == -1:
            visited[adj] = visited[cur] + 1
            q.append(adj)

# 디버깅시 내가 테스트한 케이스들은 ㄱㅊ은데, 제출에서 틀렸다고 하는 경우는 if 조건을 잘 살펴보자. 
# 이 문제의 경우는 n과 k가 0~100000이므로, if 0 <= adj < max 