N, M = map(int, input().split())
arr = [input() for _ in range(N)]
answer = []

for i in range(N-7):
    for j in range(M-7):
        start_w = 0 # w 시작일 때 바꿔야 할 개수
        start_b = 0 # b 시작일 때 바꿔야 할 개수
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l)%2 == 0:
                    if arr[k][l] == "B":
                        start_w += 1
                    else:
                        start_b += 1
                else:
                    if arr[k][l] == "B":
                        start_b += 1
                    else:
                        start_w += 1
        
        answer.append(start_w)
        answer.append(start_b)
print(min(answer))