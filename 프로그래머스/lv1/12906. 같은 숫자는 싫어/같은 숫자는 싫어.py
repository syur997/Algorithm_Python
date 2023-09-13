def solution(arr):
    x = []
    x.append(arr[0])
    for i in arr:
        if x[-1] != i:
            x.append(i)
    return x