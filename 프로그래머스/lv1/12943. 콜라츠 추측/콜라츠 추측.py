def solution(num):
    x = 0
    while num != 1:
        if x < 500:
            x += 1
            if num % 2 == 0:
                num /= 2
            elif num % 2 == 1:
                num = num * 3 + 1
        else:
            return -1
    return x