from collections import deque

def solution(priorities, location):
    q = [[idx, pri] for idx, pri in enumerate(priorities)]
    out = 0
    
    while q:
        pop = q.pop(0)

        for i in range(len(q)):
            if pop[1] < q[i][1]:
                q.append(pop)
                break
            if i == len(q)-1:
                out += 1
                if pop[0] == location:
                    return out
    return out


# 후.. 틀림