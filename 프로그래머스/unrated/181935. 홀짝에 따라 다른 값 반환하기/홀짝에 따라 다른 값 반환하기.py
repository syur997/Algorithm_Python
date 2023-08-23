def solution(n):
    x = 0
    if n % 2 == 1:
        for i in range(1, n+1, 2):
            x += i
        return x
    else:
        for i in range(0, n+1, 2):
            i = i ** 2
            x += i
        return x