def solution(array):
    x = ''
    for i in array:
        x += str(i)
    for j in x:
        if j != '7':
            x = x.replace(j, '')
    return len(x)