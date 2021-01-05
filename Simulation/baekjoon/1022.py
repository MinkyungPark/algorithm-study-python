# 다시 풀어야됨

# 내가 한거
import sys
input = sys.stdin.readline

r1,c1,r2,c2 = map(int, input().split())

ma = [[] for _ in range(r2-r1+1)]

for row in ma:
    c = c1
    for col in range(c2-c1+1):
        row.append([r1,c,max(abs(r1), abs(c))])
        c += 1
    r1 += 1


for row in ma:
    for col in row:
        case = col[0] - col[1]
        val = (2*col[2]+1)**2
        if case == 0 and col[0] > 0:
            col.append(val) # 4
        elif case == 0 and col[0] < 0:
            col.append(val - (2*col[2])*2) # 1
        elif case == -2*col[2]: 
            col.append(val - (2*col[2])*3) # 2
        elif case == 2*col[2]:
            col.append(val - (2*col[2])) # 3
        else:
            if col[0] == -col[2]: # 위
                col.append(val - (2*col[2])*2 - (col[2]+col[1]))
            elif col[0] == col[2]: # 아래
                col.append(val - (col[2]-col[1]))
            elif col[1] == col[2]: # 오른
                col.append(val - (2*col[2])*3 - (col[2]+col[0]))
            else: # 왼쪽
                col.append(val - (2*col[2]) - (col[2] - col[0]))

max_len = 0
for row in ma:
    max_tmp = max(map(len, [str(col[3]) for col in row]))
    if max_len < max_tmp:
        max_len = max_tmp
    for col in row:
        print("{0:{1}d}".format(col[3], max_len), end=" ")
    print()
