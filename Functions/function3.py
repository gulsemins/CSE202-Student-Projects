def filter(list, function):
    filteredList = []
    for n in range(len(list)):
        if function(list[n]):
            filteredList.append(list[n])
    return filteredList

numbers = [1, 2, 3, 4, 5]
def checkOdd(number):
    return number %2!=0
oddNumbers = filter(numbers, checkOdd)

print(oddNumbers)  