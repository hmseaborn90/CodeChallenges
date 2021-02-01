def name_shuffler(str_):
    missyElliot = str_.split(' ')[::-1]
    delimiter = ' '
    single_str = delimiter.join(missyElliot)
    return single_str





def name_shuffler(str_):
#     [first, last] = str_.split()
#     return (f'{last} {first}')
    
    missyElliot = ' '.join(str_.split(' ')[::-1])
    return (missyElliot)

#  just flip it and reverse it