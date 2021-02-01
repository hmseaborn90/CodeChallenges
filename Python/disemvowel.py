
def disemvowel(string):
    vowel_set = {"a","e","i","o","u"}
    output = ""
    vowels = ""
    for i in string:
        if i.lower() in vowel_set:
            vowels += i
        else:
            output += i
    return output

    def disemvowel(string):
    return "".join(c for c in string if c.lower() not in "aeiou")