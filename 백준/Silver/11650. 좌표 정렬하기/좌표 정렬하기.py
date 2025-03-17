arr = []
for _ in range(int(input())):
    arr.append(list(map(int, input().split())))

arr = sorted(arr, key=lambda x : x[1])
arr = sorted(arr, key=lambda x : x[0])

[print(*i) for i in arr]