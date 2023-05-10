#The memoize() function takes a function fn as an argument.'memoize' returns another function 'inner' that memoizes the results of 'fn'.
def memoize(fn):     
    cache = {}
    def inner(*args):
        x= str(args)
        if x in cache:
            return cache[x]
        else:
            result = fn(*args)
            cache[x] = result
            return result
    return inner
#The code defines a function fib that computes the nth Fibonacci number recursively. 
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

memoized_fib = memoize(fib)
print(memoized_fib(20))
#The code calls 'memoized_fib(20)' to compute the 20th Fibonacci number, using the memoized version of the function.
    

   