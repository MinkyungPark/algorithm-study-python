from collections import deque

def solution(prices):
    answer = []
    q = deque(prices)
    
    while q:
        pop = q.popleft()
        
        if len(q) == 0:
            answer.append(0)
        else:
            time = 0
            for comp in q:
                time += 1
                if pop > comp:
                    break
            answer.append(time)
    
    return answer


#  스택으로 하면 시간초과