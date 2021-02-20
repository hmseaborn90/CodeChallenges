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
    print(output)