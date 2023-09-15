def solution(sizes):
    x = []
    y = []
    for i in range(len(sizes)):
        x.append(max(sizes[i]))
        y.append(min(sizes[i]))
    return max(x) * max(y)