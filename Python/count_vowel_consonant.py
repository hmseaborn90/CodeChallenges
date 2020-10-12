def countVowelConsonant(s):
    counter = 0
    for i in s:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            counter += 1
        else:
            counter +=2
    return counter