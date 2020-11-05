def first_not_repeating_character(s):
    count = {}
    for c in s:
        if c not in count.keys():
            count[c] = 1
        else:
            count[c] += 1
            
    for num in count:
        if count[num] == 1:
            return num
    return "_"


first_not_repeating_character('abacabad')