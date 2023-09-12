def solution(a, b):
    x = 0
    for i in range(len(a)):
        x += a[i] * b[i]
    return x