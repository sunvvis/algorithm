arr = []

for _ in range(int(input())):
    age, name = input().split()
    arr.append([int(age), name])


for i in sorted(arr, key=lambda x: x[0]):
    print(i[0], i[1])