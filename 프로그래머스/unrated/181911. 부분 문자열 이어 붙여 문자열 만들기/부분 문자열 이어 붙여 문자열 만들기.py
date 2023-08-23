def solution(my_strings, parts):
    x = ''
    for idx, val in enumerate(parts):
        x += my_strings[idx][val[0]:val[1]+1]
    return x