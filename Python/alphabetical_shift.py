def alphabeticShift(inputString):
    result = ''
    for i in inputString:
        if ord(i) == 122:
            result += 'a'
        else:
            result += chr(ord(i) + 1)
    return result
