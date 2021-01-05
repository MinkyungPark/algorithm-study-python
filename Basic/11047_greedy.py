def greedy(coins, k):
    coins = reversed(coins)
    count = 0
    total = k
    for coin in coins:
        if coin <= total and total % coin >= 0:
            cnt = total // coin
            count += cnt
            total -= coin*cnt
        if total == 0:
            break
    return count

if __name__ == "__main__":
    n, k = map(int, input().split())
    coins = []
    for i in range(n):
        coins.append(int(input()))
    print(greedy(coins, k))


'''
n, k = map(int, input().split())
m = []
num = 0
for i in range(n):
    m.append(int(input()))
for i in range(n - 1, -1, -1):
    if k == 0:
        break
    if m[i] > k:
        continue
    num += k // m[i]
    k %= m[i]
print(num)
'''