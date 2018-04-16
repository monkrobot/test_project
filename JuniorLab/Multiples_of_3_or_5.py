def func(n):
    numbers = [x for x in range(n) if x%3 == 0 or x%5 == 0]
    return sum(numbers)

print(func(3))
