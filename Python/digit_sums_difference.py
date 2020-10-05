def digitSumsDifference(n):
    sumOdd = 0
    sumEven = 0
    for i in str(n):
        if (int(i) % 2 == 0): 
            sumEven += int(i) % 10
        else: 
            sumOdd += int(i) % 10
    return(sumEven - sumOdd)

print(digitSumsDifference(412))