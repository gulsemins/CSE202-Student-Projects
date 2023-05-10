#--------------------function1 test cases

def test_map_make_even():
    # Test an empty list
    assert map_make_even(make_even, []) == []
    
    # Test a list of even numbers
    assert map_make_even(make_even, [2, 4, 6, 8]) == [2, 4, 6, 8]
    
    # Test a list of odd numbers
    assert map_make_even(make_even, [1, 3, 5, 7]) == [2, 4, 6, 8]
    
    # Test a mixed list of even and odd numbers
    assert map_make_even(make_even, [1, 2, 3, 4, 5, 6]) == [2, 2, 4, 4, 6, 6]
    
    # Test a large list of random numbers
    import random
    nums = [random.randint(1, 1000) for _ in range(10000)]
    expected_output = [num+1 if num%2==1 else num for num in nums]
    assert map_make_even(test_map_make_even, nums) == expected_output
    
test_map_make_even()

#--------------------function2 test cases
def test_memoize():
    # Test for a small value of n
    @memoize
    def small_fib(n):
        if n < 2:
            return n
        return small_fib(n - 1) + small_fib(n - 2)
    assert small_fib(6) == 8

    # Test for repeated function calls
    count = [0]
    @memoize
    def repeat_func(n):
        count[0] += 1
        return n * n
    repeat_func(5)
    repeat_func(5)
    repeat_func(5)
    assert count[0] == 1

test_memoize()

#--------------------function3 test cases


def checkOdd(number):
    return number % 2 != 0
assert filter(numbers, checkOdd) == []
#Expected output: An empty list, since there are no odd numbers in the input list.

#Test with an empty list and an odd checker function: 
numbers = []
def checkOdd(number):
    return number % 2 != 0
assert filter(numbers, checkOdd) == []
#Expected output: An empty list, since there are no numbers in the input list.

#--------------------function4 test cases
def test_compose():
    f = lambda x: x * 2
    g = lambda x: x + 3
    h = compose(f, g)
    assert h(4) == 14
    
    f = lambda x: x**2
    g = lambda x: x + 1
    h = compose(f, g)
    assert h(3) == 16

    f = lambda x:  x.upper()
    g = lambda x:  x.replace("e", "a")
    h = compose(f, g)
    assert h() == ""

test_compose()

#--------------------function5 test cases

def test_reduce():
    numbers = [1, 2, 3, 4, 5]
    assert reduce(sum_reducer, 0, numbers) == sum(numbers)
    
    words = ["apple", "banana", "orange"]
    assert reduce(lambda x, y: x + y, "", words) == "applebananaorange"
    
    letters = ["a", "b", "c"]
    assert reduce(lambda x, y: x + y, "", letters) == "abc"
    
test_reduce()

