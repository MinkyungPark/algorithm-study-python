def solution(s):
    answer = 0
    result = []
    for i in range(1,len(s)+1):
        pre = s[:i]
        count = 1
        tmp = ""

        for j in range(i,len(s),i):
            if s[j:j+i] == pre:
                count += 1
                pre = s[j:j+i]
            else:
                if count == 1:
                    tmp += pre
                else:
                    tmp += str(count)+pre
                pre = s[j:j+i]
                count = 1
        if count == 1:
            tmp += pre
        else:
            tmp += str(count)+pre

        result.append(len(tmp))

    answer = min(result)

    return answer