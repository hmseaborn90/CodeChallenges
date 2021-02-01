def digital_root(n):
    digits = [int(d) for d in str(n)]
    total = 0
    for i in digits:
        total += i
    if total < 10:
        return total
    return digital_root(total)