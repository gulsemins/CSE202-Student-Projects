#The code defines a function compose that takes two functions as parameters, f and g. The compose function generates a new function with a single input, x. When called with x, the returned function applies the function g to x and then the function f to the result of g(x).
def compose(f, g):
    return lambda x: f(g(x))

def add(x):
    return x + 6
# Function to add 6
def square(x):
    return x * x
#The code defines two other functions: add(x) and square(x). The add function takes a number x and adds 6 to it. The square function takes a number x and returns its square.
composed_func = compose(square, add)
#The resulting function is assigned to the variable composed_func.
result = composed_func(2)

print(result)