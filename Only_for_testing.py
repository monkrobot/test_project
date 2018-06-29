def func_generator():
    for i in range(10):
        yield i+100

x=func_generator()
print(next(x))
print(next(x))