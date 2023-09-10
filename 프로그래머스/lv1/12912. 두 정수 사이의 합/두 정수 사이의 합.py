def solution(a, b):
    x = [a, b]
    return sum(i for i in range(min(x), max(x)+1))