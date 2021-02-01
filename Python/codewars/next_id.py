def next_id(arr):
    if not arr: return 0
    sorted_arr = sorted(arr)
    if sorted_arr[0] is not 0: return 0
    start = sorted_arr[0]
    size = len(sorted_arr)
    for i in range(size):
        if sorted_arr[i] == start or sorted_arr[i] == (start + 1):
            start = sorted_arr[i]
    return start + 1




def next_id(arr):
    for i in range(len(arr)+1):
        if i not in arr:
            return i



def next_id(arr):
    if not len(arr): return 0
    d = set(sorted(arr))
    a = set(range(0, max(d) + 1))
    m = a - d
    if m:
        return min(m)
    else:
        return 0 if 0 not in d else max(d) + 1

def next_id(a):
    i = 0
    set_a = set(a)
    while i in set_a:
        i += 1
    return i