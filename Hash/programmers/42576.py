# 첫번째 풀이
# def solution(participant, completion):
#     hash = {}
#     for p in participant:
#         if p not in hash:
#             hash.setdefault(p,1) # hash[p] = 1
#         else:
#             hash[p] += 1
    
#     for c in completion:
#         if hash[c] == 1:
#             del hash[c]
#         else:
#             hash[c] -= 1

#     return list(hash.keys())[0]

# 두번째 풀이
# from collections import Counter

# def solution(participant, completion):
#     answer = Counter(participant) - Counter(completion)
#     return list(answer.keys())[0]

# p = ['a','b','c']
# c = ['a','b']
# print(solution(p,c))

    
# 세번째 풀이
def solution(participant, completion):
    hash = {part:0 for part in participant}
    
    for part in participant:
        hash[part] += 1
    
    for comp in completion:
        hash[comp] -= 1
        
    answer = [key for key in hash.keys() if hash[key] > 0][0]
    
    return answer