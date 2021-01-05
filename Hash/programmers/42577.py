
# 1. Hash
# list 그대로 for item in list 해도 되지만, 딕셔너리가 빠름

def solution(phone_book):
    answer = True
    hash_map = {number:0 for number in phone_book}

    for number in phone_book:
        tmp = ""
        for num in number:
            tmp += num
            if tmp in hash_map and tmp != number:
                answer = False
                break

    return answer

# 2. sort와 startswith()를 사용한 방법. 
# sort를 쓰면 느리다. startwith를 두번하는게 더 빠름
def solution(phone_book):
    answer = True
    pb = sorted(phone_book)
    
    for i in range(len(pb)-1):
        if pb[i+1].startswith(pb[i]) == True:
            # 더긴스트링.startwith(더짧은스트링)
            answer = False
            break
    
    return answer

p = ["119", "97674223", "1195524421"]
print(solution(p))