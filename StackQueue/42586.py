from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    days = []

    for i in range(len(progresses)):
        days.append(math.ceil(((100-progresses[i]) / speeds[i])))

    q = deque(days)
    origin = q.popleft()
    num = 1

    while q:
        comp = q.popleft()
        if origin >= comp:
            num += 1
        else:
            answer.append(num)
            num = 1
            origin = comp

    return answer + [num]


# 11-24 라인

# 다른풀이 보기