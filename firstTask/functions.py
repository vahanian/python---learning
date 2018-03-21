#struktura funkcji
def calculateSum(array):
    sum = 0
    for element in array:
        sum = sum + element
    
    return sum

def calculateAverage(array):
    sum = calculateSum(array)

    return sum / len(array)


# def nazwa_funkcji(argumenty_funkcji):
#     cialo funkcji
#     .
#     .
#     .
#     .
