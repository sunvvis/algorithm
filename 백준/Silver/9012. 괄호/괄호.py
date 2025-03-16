for i in range(int(input())):
    count = 0
    ps = list(input().strip())
    for j in ps:
        if j == "(":
            count += 1 
        elif j == ")":
            count -= 1
        if count < 0:
            break
    if count == 0:
        print("YES")
    else:
        print("NO")