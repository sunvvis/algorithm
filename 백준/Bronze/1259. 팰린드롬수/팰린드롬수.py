while True:
    text = input()
    if text == "0":
        break
    print("yes") if text == text[::-1] else print("no")
