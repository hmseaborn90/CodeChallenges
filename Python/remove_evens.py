def removeEvens(numbers):
    for i in numbers:
        if i % 2 == 0:
            numbers.remove(i)   
    return numbers

def removeEvens(numbers):
    return [i for i in numbers if i % 2 != 0]
