def solution(n):
    x = 1
    for i in range(1, 11):
        if x * i < n:
            x = x * i
        elif x * i == n:
            return i
        else:
            return i - 1        