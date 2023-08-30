def solution(balls, share):
    bf = 1
    sf = 1
    result_f = 1
    for i in range(1, balls+1):
        bf *= i
    for j in range(1, share+1):
        sf *= j
    for k in range(1, balls-share+1):
        result_f *= k
    return bf / (result_f * sf)