def descending_order(num):
    sorted_list = sorted(list(str(num)))
    return int(''.join(sorted_list[::-1]))

def Descending_Order(num):
return int("".join(sorted(str(num), reverse=True)))
