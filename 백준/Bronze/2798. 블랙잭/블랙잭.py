from itertools import combinations

N, M = map(int, input().split())
arr = list(combinations(map(int, input().split()), 3))
answer = 0

for i in arr:
    if sum(i) <= M:
        if sum(i) > answer:
            answer = sum(i)

print(answer)