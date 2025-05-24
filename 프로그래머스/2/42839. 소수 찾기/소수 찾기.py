from itertools import permutations

def solution(numbers):
    answer = list(map(int, numbers))
    for i in range(len(numbers)):
        for p in permutations(answer, i+1):
            print(p)
    # for i in answer:
    #     # print(i)
    #     a = ""
    #     for j in i:
    #         a += str(j)
        # print(a)
    # return answer