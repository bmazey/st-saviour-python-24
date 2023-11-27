def fibonacci(position: int) -> int:

    list = []
    if position < 0:
        return 0
    if position >= 0 and position <= 1:
        return 1
    
    i = 2
    list[0] = 1
    list[1] = 1

    while i <= position:
        list[i] = list[i-1] + list[i-2]
        i += 1
    return list[-1]
