def solution(x):
    y = list(map(int, str(x)))
    if x % sum(y) == 0:
        return True
    else:
        return False