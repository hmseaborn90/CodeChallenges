def comp(array1, array2):
    array1.sort()
    array2.sort()
#     test = [x * x for x in array1]
#     print(test)
    if [(x,y) for x in array1 for y in array2 if x * x == y]:
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