def oddNumbersBeforeZero(sequence):

    result = 0
    for i in range(0, len(sequence)):
        if sequence[i] == 0:
            break
        if sequence[i] % 2 == 1:
            result += 1
    return result


print(oddNumbersBeforeZero([1, 2, 3, 0, 4, 5, 6, 0, 1]))