def solution(d, budget):
    d = sorted(d)
    x = []
    for i in d:
        x.append(i)
        if sum(x) > budget :
            x.pop()
            return len(x)
    return len(x)