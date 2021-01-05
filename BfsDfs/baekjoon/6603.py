'''
import sys
input = sys.stdin.readline
from itertools import combinations


while True:
    case = list(input().split())
    if case[0] == '0': break

    for result in combinations(case[1:], 6):
        print(' '.join(result))
    print()
'''

# dfs 백트래킹

def dfs_comb(lis, n):
    stack = []
    result = []
    for i in range(len(lis)-1):
        stack.append([i])
    
    while stack:
        cur = stack.pop()
        if len(cur) != n:
            for i in range(cur[-1]+1,len(lis)):
                tmp = cur + [i]
                stack.append(tmp)
        else:
            result.append(cur)
    result.sort()
    return result


while True:
    case = list(input().split())
    if case[0] == '0': break
    case = case[1:]
    for line in dfs_comb(case, 6):
        for comp in line:
            print(case[comp], end=' ')
        print()
    print()