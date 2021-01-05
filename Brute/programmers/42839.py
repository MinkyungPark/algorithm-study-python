from itertools import permutations

def solution(numbers):
    number = list(numbers)
    perms = []
    answer = 0

    for i in range(1, len(number)+1):
        for perm in permutations(number, i):
            perms.append(''.join(perm))
    perms = list(set(perms))

    for num in perms:
        if num[0] != '0' and num != '1':
            if prime_number(num) == True:
                answer += 1

    return answer

def prime_number(number):
    num = int(number)
    for f in range(2, int(num**0.5)+1):  
        if num % f == 0:     
            return False   

    return True         

numbers = "011"
solution(numbers)