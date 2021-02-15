import re
def solution(s):
    return re.sub(r"(\w)([A-Z])", r"\1 \2", s)



def solution(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)


def solution(s):
    final_string = ""
    for i in range(len(s)):
        char = s[i]
        if char.isupper():
            final_string += " " + char
        else:
            final_string += char
    return final_string

def solution(s):
    newStr = ""
    for letter in s:
        if letter.isupper():
            newStr += " "
        newStr += letter
    return newStr