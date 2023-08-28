def solution(s):
    s = s.split(' ')
    x = 0
    for i in range(len(s)):
        if s[i] != 'Z':
            x += int(s[i])
        else:
            x -= int(s[i-1])
    return x