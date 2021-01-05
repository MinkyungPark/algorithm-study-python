# chain, all, any, chain
# https://velog.io/@dramatic/Python-permutation-combination-%EC%88%9C%EC%97%B4%EA%B3%BC-%EC%A1%B0%ED%95%A9

from itertools import permutations

li = ['A','B','C']
print(list(permutations(li,2)))
print(list(map(''.join, permutations(li, 2))))
# .join은 문자열만임????
# [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
# ['AB', 'AC', 'BA', 'BC', 'CA', 'CB']


lis = list(i for i in range(1, 5))
# 같다.
for i in range(1,5):
     lis.append(i)

print(' '.join(list(map(str, lis))))
# [1, 2, 3, 4] ==> 1 2 3 4

lis = [1,2,3,3,4,5]
lis.remove(3)
print(lis)
lis = [1,2,3,3,4,5]
del lis[2]
print(lis)
lis.pop(0)
print(lis)
p = lis.pop()
print(lis)
print(p)

# 1차원 리스트 초기화
visit=[0 for i in range(4)]

# 2차원 리스트 초기화하기
# [[1,2],[3,4],[5,6]] 2개씩 3묶음/큰묶음->내부 3*2/3행2열 arr[행][열]
# [0][0]=1 [0][1]=2
s = [[0]*3] # 1*3
print(s)
ss = [[0]*2 for i in range(4)] # 4*2
print(ss)
for s in ss:
     print(' '.join(list(map(str, s))))

x = [1,2,3]
y = [4,5,6]
for i, j in zip(x, y):
     print(str(i) + "/" + str(j))


# 파이썬에서 H x W 2차원 리스트 초기화
arr = [[0 for i in range(w)] for j in range(h)]

arr = [[0]*w for j in range(h)]
#1차원 리스트
list1 = [0 for i in range(w)]
d = [-1]*10
# [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]

#2차원 리스트 선언만 하려면 아래와 같이.
data = [[] * n for i in range(n)]    # data: [[], [], [], []]

## input시, sys.stdin.readline으로 하면 시간 더 절약
import sys
input = sys.stdin.readline


# 딕셔너리, 키 값이 주요
g = {1:[1,2],2:[2]}
for key in g:
    print(key) # 키만 출력
    print(g[key]) # 밸류만 출력