'''
1. 순열 itertools.permutations 순서고려, 중복OK (0,1) (1,0) 은 다른것

일반적인 방법
def permute(arr):
    result = [arr[:]]
    c = [0] * len(arr)
    i = 0
    while i < len(arr):
        if c[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            result.append(arr[:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return result

itertools.permutation 이용

import itertools

pool = ['A', 'B', 'C']
print(list(map(''.join, itertools.permutations(pool)))) # 3개의 원소로 수열 만들기
print(list(map(''.join, itertools.permutations(pool, 2)))) # 2개의 원소로 수열 만들기


2. 조합 itertools.combinations 순서고려X, 중복X
사용법은 동일하다.

'''

# 1. itertools이용
# from itertools import permutations

# n = int(input())
# lis = []
# for i in range(1, n+1):
#     lis.append(i)

# result = list(permutations(lis))
# for re in result:
#     for r in re:
#         print(r, end=' ')
#     print()

# --------------------------------------------------------------------------------------------------------------------------------------

# 2. 재귀
#@@ perm([1,2,3,4], 2) = ([1]+perm([2,3,4],1)) + ([2]+perm([1,3,4],1)) + ([3]+perm([1,2,4],1)) + ([4]+perm([1,2,3],1))
#@@ comb([1,2,3,4], 1) = ([1]+comb([2,3,4],1)) + ([2]+comb([3,4],1)) + ([3]+comb([4],1))

# def perm(lis, n):
#     result = []
#     if n > len(lis): return result
#     if n == 1:
#         for li in lis:
#             result.append([li])
#     elif n > 1:
#         for i in range(len(lis)):
#             tmp = [i for i in lis]
#             tmp.remove(lis[i])
#             for j in perm(tmp, n-1):
#                 result.append([lis[i]]+j)
#     return result

# n = int(input())
# lis = list(i for i in range(1, n+1))

# for li in perm(lis,n):
#     print(' '.join(list(map(str, li))))

# --------------------------------------------------------------------------------------------------------------------------------------

# 3. bfs/dfs

# https://medium.com/@dltkddud4403/python-%EC%88%9C%EC%97%B4-%EC%A1%B0%ED%95%A9-%EA%B5%AC%ED%98%84-5e496e74621c