def solution(sizes):
    answer = []
    w, h = 0, 0
    for size in sizes:
        s = sorted(size, reverse=True)
        if s[0] > w: w = s[0]
        if s[1] > h: h = s[1]
    
    answer = w * h
    return answer