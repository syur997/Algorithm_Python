def solution(t, p):
    x = []
    for i in range(len(t)):
        if len(t[i:len(p)+i]) == len(p) and int(t[i:len(p)+i]) <= int(p):
            x.append(t[i:len(p)+i])
    return len(x)