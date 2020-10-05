def minMaxDifference(inputArray):

    indexOfMinimum = 0
    indexOfMaximum = 0

    for i in range(1, len(inputArray)):
        if inputArray[i] < inputArray[indexOfMinimum]:
            indexOfMinimum = i
        if inputArray[i] > inputArray[indexOfMaximum]:
            indexOfMaximum = i
    return inputArray[indexOfMaximum] - inputArray[indexOfMinimum]

print(minMaxDifference([1, 4, 10, 4, 2]))