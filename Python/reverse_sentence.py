def reverseSentence(sentence):
    split_words = sentence.split(" ")
    reversed_and_joined = " ".join(reversed(split_words))
    return reversed_and_joined

def reverseSentence2(sentence):
    split_words = sentence.split(" ")
    return " ".join(split_words[:: -1])

print(reverseSentence("well isn't this just nifty"))
print(reverseSentence2("nify just this isn't well"))