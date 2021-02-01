def calc(x):
    with7s = ''
    char_ords = [ord(i) for i in x]
    for i in char_ords:
        with7s += str(i)
    without7s = with7s.replace("7", "1")
    return sum([int(i) for i in with7s]) - sum([int(i) for i in without7s])

def calc(x):
    total1 = "".join(str(ord(char)) for char in x)
    total2 = total1.replace("7","1")
    return sum(int(x) for x in total1) - sum(int(x) for x in total2)


def calc(x):
    return ''.join(str(ord(ch)) for ch in x).count('7') * 6