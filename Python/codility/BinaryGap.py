def solution(N):
    count = 0
    counts = []
    is_counting = False
    test = f'{N:08b}'
    for i in test:
        if i == "0" and is_counting:
            count += 1
        if i == '1':
            is_counting = True
        if i == '1' and is_counting:
            counts.append(count)
            count = 0
            
    return max(counts)