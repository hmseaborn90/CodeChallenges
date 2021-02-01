def solution(s):
    if len(s) % 2 == 1:    
        s += '_'
    
    return [s[i:i+2] for i in xrange(0,len(s),2)]

def solution(s):
    return [(s + "_")[i:i + 2] for i in range(0, len(s), 2)]


def solution(s):
    result = []
    if len(s) % 2:
        s += '_'
    for i in range(0, len(s), 2):
        result.append(s[i:i+2])
    return result\


solution("asdfadsf")