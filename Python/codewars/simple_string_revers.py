def solve(s):
    n = len(s)
    s = list(s)
    print(n, s)
    start = 0
    end = n -1
    while(start < end):
        if(s[start] == " "):
            start += 1
            continue
        elif(s[end] == ' '):
            end -= 1
            continue
        s[start], s[end] = (s[end], s[start])
        start += 1
        end -= 1
    print(''.join(s))