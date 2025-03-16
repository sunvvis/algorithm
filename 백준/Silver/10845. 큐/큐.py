from collections import deque

deck = deque()

for _ in range(int(input())):
    cmd = input().split()
    if cmd[0] == "push":
        deck.append(cmd[1])
    elif cmd[0] == "pop":
        if len(deck) == 0:
            print(-1)
        else:
            print(deck.popleft())
    elif cmd[0] == "size":
        print(len(deck))
    elif cmd[0] == "empty":
        print(1) if len(deck) == 0 else print(0)
    elif cmd[0] == "front":
        if len(deck) == 0:
            print(-1)
        else:
            print(deck[0])
    elif cmd[0] == "back":
        if len(deck) == 0:
            print(-1)
        else:
            print(deck[-1])
