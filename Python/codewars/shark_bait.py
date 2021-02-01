def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    if shark_distance == 0:
        return "Shark Bait!"
    res = ''
    if dolphin:
        shark_speed = shark_speed / 2
    shark = shark_speed / shark_distance
    you = you_speed /pontoon_distance
    print(shark, you)
    if shark > you:
        res += "Shark Bait!"
    if shark < you:
        res += "Alive!"
    return res



    def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    if dolphin:
        shark_speed = shark_speed / 2
        
    shark_eat_time = shark_distance / shark_speed
    you_safe_time = pontoon_distance / you_speed
    
    return "Shark Bait!" if you_safe_time > shark_eat_time else "Alive!"