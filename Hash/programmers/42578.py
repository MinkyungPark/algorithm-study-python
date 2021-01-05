# 첫번째 풀이
def solution(clothes):
    answer = 1
    hash = {cloth[1]:1 for cloth in clothes}
    for cloth in clothes:
        hash[cloth[1]] += 1
    
    for value in hash.values():
        answer *= value
        
    return answer - 1


# 두번째 풀이
from functools import reduce

def solution(clothes):
    hash_map = {cloth[1]:1 for cloth in clothes}
    for cloth in clothes:
        hash_map[cloth[1]] += 1
    
    return reduce(lambda x,y:x*y, [val for val in hash_map.values()]) - 1