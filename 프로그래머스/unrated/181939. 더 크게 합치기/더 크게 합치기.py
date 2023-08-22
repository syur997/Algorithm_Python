def solution(a, b):
    x = str(a) + str(b)
    y = str(b) + str(a)
    if x > y :
        return int(x)
    elif x == y :
        return int(x)
    else :
        return int(y)