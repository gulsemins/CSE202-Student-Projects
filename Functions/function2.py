def map_make_double(make_double,numbers):
    squared_nums = []
    for n in numbers:
        squared_nums.append(make_double(n))
    return squared_nums
#This program shows how to use higher-order function map to apply the function make_double on each member of a list of numbers and return a new list of changed elements squared_nums. 
numbers =[1,2,3,4,5]
square = lambda n:n**2
squared_nums = map_make_double(square, numbers)
#Make_double is a lambda function that returns the square of the input parameter in this example. The map_make_double function accepts two inputs, a function and a list, and produces a new list with the changed elements. 
print(squared_nums)
    

    

   