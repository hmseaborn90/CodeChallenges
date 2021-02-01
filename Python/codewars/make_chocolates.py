# return the number of small chocolates required to achieve 
# the desired goal. Return -1 if the goal cannot be achieved 
def make_chocolates(small, big, goal):
    double_loop = [i for i in range(small + 1) for j in range(big + 1) if j * 5 + i * 2 == goal]
    return double_loop[0] if double_loop else -1


def make_chocolates(s,b,n):
    bigs = min(n//5,b)
    n -= 5 * bigs
    if n&1 and bigs: n+=5
    smalls = min(s,n//2)
    return -1 if n-2*smalls else smalls


def make_chocolates(small, big, goal):
b = min(big, goal // 5)
s = min(small, (goal - b * 5) / 2)
if s != int(s):
    b -= 1
    s = min(small, (goal - b * 5) // 2)
return s if b >= 0 and b * 5 + s * 2 == goal else -1


def make_chocolates(small, big, goal):
    return next((z for x in range(big, -1, -1) if (y := goal - 5*x) >= 0 and y&1^1 and (z := y>>1) <= small), -1)