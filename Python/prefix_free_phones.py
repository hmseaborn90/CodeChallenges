# def prefixFreePhones(numbers):
#     numbers.sort(key = len)
#     print(numbers)
#     first_num = numbers[0]
#     first_len =(len(numbers[0]))
#     numb_2 = numbers[1:]
#     for n in numb_2:
#         num = str(n)
#         check = int(num[:first_len])
#         print('why not',check, first_num)
#         print('bool',first_num == str(check))
#         if first_num == str(check):
#             return False
#     return True

# def prefixFreePhones(numbers):
#     numbers.sort(key=len)
#     longest = len(numbers[-1])
#     numberList = [x for x in numbers if len(x) < longest]
    
#     for num in range(0, len(numberList)):
#         num_1 = numbers[num]
#         for num_2 in numbers[num+1:]:
#             if num_1 == num_2[:len(num_1)]:
#                 return False
#     return True
    
# def prefixFreePhones(numbers):
#     # numbers.sort(key=len)
#     # longest = len(numbers[-1])
#     # numberList = [x for x in numbers if len(x) < longest]
#     for index, nElement in enumerate(numbers):
#         for compareElementIndex in range(index+1, len(numbers)):
#             print(numbers[compareElementIndex], nElement)
#             if numbers[compareElementIndex].startswith(nElement):
#                 return False
#     return True
# def prefixFreePhones(numbers):
#     set_nums = set(numbers)
#     print(set_nums)
#     for num in numbers:
#         print(num)
#         for idx in range(1, len(num)):
#             if num[:idx] in set_nums:
#                 return False
#     return True
    
def prefixFreePhones(numbers):
    # numbers.sort(key=len)
    # num_set = set()
    nums_dict = {n: True for n in numbers}
    # for n in numbers:
    #     nums_dict[n] = true
    for n in numbers:
        for prefix_len in range(1, len(n)):
            prefix =n[0:prefix_len]
            if prefix in nums_dict:
                return False
    return True



numbers = ['67179005', '671794581', '67179820', '6717978321', '671796629', '671794057', '67179562', '6717949536', '6717995403', '671792335', '671794532', '6717954616', '671796621', '67179866', '6717974097', '6717959778', '671795434', '67179814', '6717978699', '67179720', '67179917', '67179690', '671790662', '67179755', '6717929638', '6717905746', '671797553', '671793657', '67179007', '67179545', '67179586', '6717979374', '67179132', '67179510', '67179331', '6717901072', '671793166', '6717926669', '671798556', '6717970752', '671794023', '67179823', '6717992811', '671797438', '6717939862', '6717989853', '671797491', '6717992602', '6717907778', '6717911173']


print(prefixFreePhones(numbers))