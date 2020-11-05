def uncover_spy(n, trust):
    if len(trust) < n-1:
        return -1   
        
    trust_counter = [0] * (n + 1)
    
    for a, b in trust:
        trust_counter[a] -= 1
        trust_counter[b] += 1
        
    for i in range(1, n + 1):
        if trust_counter[i] == n - 1:
            return i
            
    return -1