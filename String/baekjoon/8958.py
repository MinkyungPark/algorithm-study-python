n = int(input())

for _ in range(n):
    lis = list(str(input()))
    count = [0,1]

    for li in lis:
        if li == 'O':
            count[0] += count[1]
            count[1] +=1
        else:
            count[1] = 1

    print(count[0])