def solve(a,b):
    return (''.join([str(i) for i in a if i in set(a) - set(b)])) + (''.join([str(i) for i in b if i in set(b) - set(a)]))
    # I know im sorry


def solve(a,b):
    s = set(a)&set(b)
    return ''.join(c for c in a+b if c not in s)

def solve(a,b):
return "".join([c for c in a if not c in b]+[c for c in b if not c in a])