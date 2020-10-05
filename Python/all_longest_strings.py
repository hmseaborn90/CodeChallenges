def allLongestStrings(inputArray):

    answer = [inputArray[0]]
    for i in range(1, len(inputArray)):
        if len(inputArray[i]) == len(answer[0]):
            answer.append(inputArray[i])
        if len(inputArray[i]) > len(answer[0]):
            answer = [inputArray[i]]
    return answer

# def allLongestStrings(inputArray):
#     scale=0
#     outputArray=[]
#     for i in range(len(inputArray)):
#         if len(inputArray[i]) > scale:
#             outputArray=[]
#             outputArray.append(inputArray[i])
#             scale = len(inputArray[i])
#         elif  len(inputArray[i]) == scale:
#             outputArray.append(inputArray[i])
#     return outputArray

test = ["aba", 
 "aa", 
 "adddd", 
 "vcd", 
 "aba"]

print(allLongestStrings(test))