def solution(brown, yellow):
    hap = brown + yellow
    lis = []

    for i in range(3, hap):
        if hap % i == 0:
            if i > hap//i: break
            lis.append([hap//i,i])
    
    answer = [li for li in lis if (li[0]-2)*(li[1]-2) == yellow]

    return answer[0]


brown = 24
yellow = 24
print(solution(24, 24))