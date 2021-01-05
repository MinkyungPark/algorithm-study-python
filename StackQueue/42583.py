from functools import reduce
from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    
    while bridge:
        pop = bridge.pop()
        time += 1
        
        if truck_weights:
            if hap(bridge) + truck_weights[0] <= weight:
                bridge.appendleft(truck_weights.popleft())
            else:
                bridge.appendleft(0)

    return time

def hap(lis):
    return reduce(lambda x,y:x+y, lis)


## 시간초과