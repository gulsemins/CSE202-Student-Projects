def compose(f, g):
    return lambda x: f(g(x))

def add(x):
    return x + 6

def square(x):
    return x * x

composed_func = compose(square, add)

result = composed_func(2)

print(result)