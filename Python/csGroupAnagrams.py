def csGroupAnagrams(strs):
    outputs = {}
    for word in strs:
        index = "".join(sorted(word))
        if index in outputs:
            outputs[index].append(word)
        else:
            outputs[index] = [word]
    return_val = [outputs[x] for x in outputs]
    return sorted(return_val, key=lambda x:len(x), reverse=True)
    
# def csGroupAnagrams(words):
#     groups = {}

#     for word in words:
#         index = ''.join(sorted(word))
#         if index in groups:
#             groups[index].append(word)
#         else:
#             groups[index] = [word]

#     return_value = [groups[x] for x in groups]
#     return sorted(return_value, key=lambda x: len(x), reverse=True)