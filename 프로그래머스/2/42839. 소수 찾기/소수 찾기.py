from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    nums = set()
    for i in range(1, len(numbers)+1):
        for p in permutations(list(numbers), i):
            nums.add(int(''.join(p)))
    
    answer = sum(1 for i in nums if is_prime(i))
    return answer