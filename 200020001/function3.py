#The function filter returns a new list containing just the entries from the input list that return True when the provided function is called.
def filter(list, function):
    filteredList = []
    for n in range(len(list)):
        if function(list[n]):
            filteredList.append(list[n])
    return filteredList
#The filter function is then called with the numbers list and checkOdd function as arguments. The result of this call is assigned to the variable oddNumbers. This call to filter will return a new list containing only the odd numbers from the original list of numbers.
numbers = [1, 2, 3, 4, 5]
def checkOdd(number):
    return number %2!=0
oddNumbers = filter(numbers, checkOdd)

print(oddNumbers)

