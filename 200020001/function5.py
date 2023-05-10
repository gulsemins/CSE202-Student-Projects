numbers = [1,2,3]

def sum_reducer(initial_value, current):
    return initial_value + current
#The sum_reducer function  returns the sum of these two values.

def reduce(reducer, initial_value, array):
    value = initial_value

    for i in range(len(array)):
        current_value = array[i]
        value = reducer(value, current_value)

    return value
#The sum_reducer function is applied to the initial value of 0 and each element of the numbers array in turn by the reduce function. It accomplishes this by using a for loop to iterate over the array. The reduce function transfers the current value of the accumulator (which begins as the starting value) and the current member of the array to the reducer function in each iteration, and the result is stored as the new value of the accumulator. The reduction method returns the final value of the accumulator after iterating over the full array.
sum_of_numbers_custom = reduce(sum_reducer, 0, numbers)

print(sum_of_numbers_custom) 
#In this case, the sum_reducer function is used to add up all the numbers in the numbers array, starting from an initial value of 0. So the value of sum_of_numbers_custom will be the sum of the numbers in the numbers array, which is 6.