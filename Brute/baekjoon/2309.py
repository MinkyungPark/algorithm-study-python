from itertools import combinations

# combinations 조합 순서상관x 뽑음
# permutations 순열(펄순) 순서상관 있이 뽑음

nanjang = []
for _ in range(9):
    nanjang.append(int(input()))

for case in combinations(nanjang, 7):
    if sum(case) == 100:
        case = sorted(case)
        for c in case: print(c)
        break