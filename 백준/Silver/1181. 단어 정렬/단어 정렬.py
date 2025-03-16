import sys

N =int(input())
arr=[]
for i in range(N):
    arr.append(sys.stdin.readline())
arr=list(set(arr))
arr.sort(key=lambda x:(len(x),x))
[print(i.strip()) for i in arr]