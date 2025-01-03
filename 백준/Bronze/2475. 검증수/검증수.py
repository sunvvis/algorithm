def square(x):
    return pow(int(x), 2)


numbers = map(square, input().split())
print(sum(numbers) % 10)
