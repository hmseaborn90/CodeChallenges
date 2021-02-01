def mxdiflg(a1, a2):
    if not a1 or not a2:
        return -1
    minA1, maxA1 = min(len(ele) for ele in a1), max(len(ele) for ele in a1)
    minA2, maxA2 = min(len(ele) for ele in a2), max(len(ele) for ele in a2)
    dif1 = maxA1 - minA2
    dif2 = maxA2 - minA1
    return max(dif2, dif1)

def mxdiflg(a1, a2):
    if a1 and a2:
        return max(
            len(max(a1, key=len)) - len(min(a2, key=len)),
            len(max(a2, key=len)) - len(min(a1, key=len)))
    return -1