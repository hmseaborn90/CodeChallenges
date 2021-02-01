def pairs(ar):
    count = 0
    for i in range(0, len(ar), 2):
        
        chunk = ar[i:i + 2]
        if (len(chunk) < 2):
            return count
        elif (chunk[0] +1) == chunk[1] or (chunk[0] - 1) == chunk[1]:
            count +=1
    return count



def pairs(ar):
    res=0
    for i in range(1,len(ar),2):
        if abs(ar[i]-ar[i-1])==1:
            res+=1
    return res 


def pairs(ar):
    count = 0
    for i in range(0, len(ar), 2):
        try:
            a, b = ar[i], ar[i+1]
        except IndexError:
            return count
        
        if abs(a-b) == 1: 
            count +=1
        
    return count