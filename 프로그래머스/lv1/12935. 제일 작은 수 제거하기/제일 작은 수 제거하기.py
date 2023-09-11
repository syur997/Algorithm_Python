def solution(arr):
    arr.pop(arr.index(min(arr)))
    if arr:
        return arr
    else:
        arr.append(-1)
        return arr