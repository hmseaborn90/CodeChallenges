def csWordPattern(pattern, a):
    words = a.split()
    test = set(pattern)
    test2 = set(words)
    print(test, test2)
    return len(test) == len(test2)
    # words = a.split()
    # print(len(words), len(pattern))
    # pattern_dic = {}
    # word_dic = {}
    # for letter, word in range(len(pattern)):
    #     pattern_dic[letter] = word
    # print(pattern_dic)

