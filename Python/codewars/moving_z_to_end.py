def move_zeros(array):
    print(array)
    non_z = []
    zeros = []
    for i in range(len(array)):
        if array[i] == 0:
            if type(array[i]) == int or type(array[i]) == float:
                zeros.append(0)
            else:
                non_z.append(array[i])
        else:
            non_z.append(array[i])
    
    return(non_z + zeros)


def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))



def move_zeros(array):
    newarr =[]
    zeroarr=[]
    for item in array:
        if item!= 0 or type(item)== bool :
            newarr.append(item)
        else:
            zeroarr.append(item)
            
            
    newarr.extend(zeroarr)
    return(newarr)