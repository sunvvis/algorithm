N = int(input())
arr = map(int, input().split())

def is_prime_number(x):
    if x == 1:
        return 0
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

answer = 0
for i in arr:
    answer += is_prime_number(i)
print(answer)