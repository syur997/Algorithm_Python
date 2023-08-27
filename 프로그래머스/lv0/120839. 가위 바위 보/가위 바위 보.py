def solution(rsp):
    x = ''
    for i in rsp:
        if i == '0':
            x += '5'
        elif i == '2':
            x += '0'
        else:
            x += '2'
    return x