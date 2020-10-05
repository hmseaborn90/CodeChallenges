def digitsManipulations(n):
    total_sum = 0
    product = 1
    while (n != 0):
        product = product * (int(n % 10))
        total_sum = total_sum + int(n % 10)
        n = int(n // 10)
        print(n)

    final = product - total_sum
    return final

    # def digitsManipulations(n):
#     m = n
    
#     product = 1
#     while(n != 0):
        
#         product = product*(int(n%10))
#         n = int(n//10)
    
#     total = 0
#     while(m != 0):
#         total = total + int(m%10)
#         m = int(m//10)
#         print(m)
#     final = product - total
#     return final
        

# def digitsManipulations(n):
#     strNum = str(n)
#     array_nums = [i for i in range(1, len(strNum))]
#     print(array_nums)
#     for item in range(0, len(array_nums)):
#         print(int(strNum[item]) * int(strNum[item + 1]))
#     # for i in productuct:
#     #     n = int(i)
#     #     print(n * n)
        
print(digitsManipulations(123456))