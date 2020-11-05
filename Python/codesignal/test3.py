def uncover_spy(n, trust):

    trust_counter = [0] * (n + 1)
    
    
    for a, b in trust:
        trust_counter[a] -= 1
        trust_counter[b] += 1

    for i in range(1, n + 1):
        if trust_counter[i] == n - 1:
            return i
            
    return -1
    
uncover_spy(3, [[1, 3], [2, 3]])