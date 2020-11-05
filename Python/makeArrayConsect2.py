def makeArrayConsecutive2(statues):
    s_stat = sorted(statues)
    missing_statues = [x for x in range(s_stat[0], s_stat[-1]+1)if x not in s_stat]
    return len(missing_statues)



def makeArrayConsecutive2(statues):
return max(statues) - min(statues) - len(statues) + 1
