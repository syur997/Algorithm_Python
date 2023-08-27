def solution(arr):
    x = []
    for i in range(len(arr)):
        if arr[i] == 2:
            x.append(i)
    if x == []:
        return [-1]
    else:
        return arr[x[0]:x[-1]+1]