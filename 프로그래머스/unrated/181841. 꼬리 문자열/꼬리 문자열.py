def solution(str_list, ex):
    x = ''
    for i in range(len(str_list)):
        if ex not in str_list[i]:
            x += str_list[i]
        else:
            pass
    return x