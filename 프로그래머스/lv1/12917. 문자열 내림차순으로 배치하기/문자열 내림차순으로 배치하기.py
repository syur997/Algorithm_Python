def solution(s):
    return ''.join(sorted(list(map(str, s)), reverse=True))