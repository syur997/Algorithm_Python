def solution(arr, k):
    x = []
    for i in arr:
        if i not in x:
            x.append(i)
    for j in range(k):
        if len(x) == k:
            return x[:k]
        else:
            x.append(-1)
    return x[:k]