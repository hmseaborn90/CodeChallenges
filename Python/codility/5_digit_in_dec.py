# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    n_string = str(N)
    for i in range(len(n_string) +1):
        if i == 0 and n_string[0] == "-":
            n_string = n_string[:i+1] + "5" + n_string[i+1:]
        elif int(n_string[i]) < 5:
            n_string = n_string[:i] + "5" + n_string[i:]
            break
    return int(n_string)
