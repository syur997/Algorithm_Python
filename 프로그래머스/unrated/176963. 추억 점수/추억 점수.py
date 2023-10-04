def solution(name, yearning, photo):
    x = dict(zip(name, yearning))
    y = []
    for i in photo:
        z = 0
        for j in i:
            if j in x:
                z += x[j]
        y.append(z)
    return y