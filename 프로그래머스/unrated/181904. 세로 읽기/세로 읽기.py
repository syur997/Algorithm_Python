def solution(my_string, m, c):
    x = ''
    for i in range(c-1, len(my_string), m):
        x += my_string[i]
    return x