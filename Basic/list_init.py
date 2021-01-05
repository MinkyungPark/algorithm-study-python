# 2차원 리스트 생성 

# 내가 원래 쓰던 방법 for 반복문
a = []
for i in range(3):
    tmp = []
    for j in range(2):
        tmp.append(0)
    a.append(tmp)
print(a)
# [[0, 0], [0, 0], [0, 0]]


# 리스트 표현식 사용.
b = [[0 for j in range(2)] for i in range(3)]
c = [[0]*2 for i in range(3)]
# [0]*2 = [0,0]
print(b)
print(c)
# [[0, 0], [0, 0], [0, 0]]
# [[0, 0], [0, 0], [0, 0]]


# 톱니형 리스트
# [[0, 0, 0], [0], [0, 0, 0], [0, 0], [0, 0, 0, 0, 0]]
a = [3,1,3,2,5]
b = []
for i in a:
    tmp = []
    for j in range(i):
        tmp.append(0)
    b.append(tmp)
print(b)

a = [[0]*i for i in [3,1,3,2,5]]
print(a)

#
li = [5]
# [,,,,]