def solution(arr, divisor):
    x = sorted([i for i in arr if i % divisor == 0])
    if x:
        return x
    else:
        return [-1]