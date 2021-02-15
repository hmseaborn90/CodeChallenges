from collections import Counter
def anagrams(word, words):
    return [w for w in words if Counter(w) == Counter(word)]


def anagrams(word, words): return [item for item in words if sorted(item)==sorted(word)]