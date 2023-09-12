def solution(s):
    x = len(s) // 2
    if len(s) % 2 == 1:
        return s[x]
    else:
        return s[x-1:x+1]