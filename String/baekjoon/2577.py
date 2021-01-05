gop = int(input()) * int(input()) * int(input())
lis = [0] * 10
for num in list(map(int, str(gop))):
    lis[num] += 1

for li in lis:
    print(li)