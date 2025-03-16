arr = []
for _ in range(int(input())):
    arr.append(input())

arr = list(set(arr))
arr.sort()
arr.sort(key=len)
[print(i) for i in arr]
