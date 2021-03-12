def elevator_distance(array):
    i = 0
    output = 0
    while i < len(array) -1:
        one, two = array[i], array[i+1]
        if one >= two:
            output += (one-two)
            i+=1
        else:
            output += (two-one)
            i+=1
    return output

def elevator_distance(array):
    output, i = 0,0
    while i < len(array) -1:
        output += abs(array[i] - array[i+1])
        i+=1
    return output


def elevator_distance(array):
    return sum(abs(a - b) for a, b in zip(array, array[1:]))



# like the zip of an array and array slicing off the first index 
def elevator_distance(array):
    print(array)
    print(array[1:])
#     test = zip(array, array[1:])
#     print(test)
    for a,b in zip(array,array[1:]):
        print(a,b)
    # return sum(abs(a - b) for a, b in zip(array, array[1:]))
    
# elevator_distance([2,5,6,7])