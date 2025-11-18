def zoek(gesorteerd: list, x: int):
    low = 0
    high = len(gesorteerd) - 1

    while high >= low:
        mid = (low + high) // 2
        if x < gesorteerd[mid]:
            high = mid - 1
        elif x == gesorteerd[mid]:
            return mid
        else:
            low = mid + 1

    return None


        
    
