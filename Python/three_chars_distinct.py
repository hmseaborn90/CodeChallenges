def threeCharsDistinct(s):
    def distinct_tuple(trio):
        if trio[0] != trio[1] and trio[0] != trio[2] and trio[1] != trio[2]: 
            return True
        else: 
            return False
    count = 0
    n = len(s)
    print(type(s), type(n))
    if n < 3: return 0
    for i in range(n-2):
        print(s[i:i+3])
        if distinct_tuple(s[i:i+3]): count += 1
    return count

#with is not instead
def threeCharsDistinct2(s):
    def distinct_tuple(trio):
        if trio[0] is not trio[1] and trio[0] is not trio[2] and trio[1]  is not trio[2]: 
            return True
        else: 
            return False
    count = 0
    n = len(s)
    print(s)
    if n < 3: return 0
    for i in range(n-2):
        print(s[i:i+3])
        if distinct_tuple(s[i:i+3]): count += 1
    return count

print(threeCharsDistinct("abcdaaae"))
print(threeCharsDistinct2("abcdaaae"))