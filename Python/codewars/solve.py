def solve(a,b):
    d = {}
    for chars in b:
        d[chars] = 0
    for chars in a:
        if chars in d:
            d[chars] += 1
    return list(d.values())

def sove(a,b):
    return [a.count(chars) for chars in b]

def solve(a,b):
    return [a.count(e) for e in b]

def solve(haystack, needles):
    return [haystack.count(needle) for needle in needles]