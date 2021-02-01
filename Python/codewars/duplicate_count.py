def duplicate_count(text):
    count_let = {}
    dup_count = 0
    for i in text:
        lower = i.lower()
        if lower not in count_let.keys():
            count_let[lower] = 1
        else:
            count_let[lower] += 1
            
    for num in count_let:
        if count_let[num] > 1:
            dup_count += 1
    return dup_count
     
def duplicate_count(text):
    count = 0
    for c in set(text.lower()):
        if text.lower().count(c) > 1:
            count += 1
    return count
     
def duplicate_count(s):
    return len([c for c in set(s.lower()) if s.lower().count(c)>1])
     