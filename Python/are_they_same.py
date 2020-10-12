def comp(array1, array2):
    array1.sort()
    array2.sort()
#     test = [x * x for x in array1]
#     print(test)
    if [(x,y) for x in array1 for y in array2 if x * x == y]:
        return True
def comp(array1, array2):
    try:
        return sorted([num ** 2 for num in array1]) == sorted(array2)
    except:
        return False
# def comp(array1, array2):
#     if array1 is None or array2 is None:
#         return False
#     print(type(array1), type(array2))
#     result = [x for x in zip(sorted(array1), sorted(array2))]
#     print(result)
#     if [(x,y) for x, y in result if x * x != y]:
#         return False
#     return True
def comp(array1, array2):
    if array1 is None or array2 is None:
        return False
    print(array1, array2)
    print(type(array1), type(array2))
    result = [x for x in zip(sorted(array1), sorted(array2))]
    print(result)
    for x, y in result:
        
        if abs(x)*abs(x) != abs(y):
            return False
    return True
a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
print(comp(a1, a2), True)


number_list = [1, 2, 3]
str_list = ['one', 'two', 'three']

# No iterables are passed
result = zip(number_list, str_list)

# Converting itertor to list
result_list = list(result)
print(result_list)

# Two iterables are passed
result = zip(number_list, str_list)

# Converting itertor to set
result_set = set(result)
print(result_set)