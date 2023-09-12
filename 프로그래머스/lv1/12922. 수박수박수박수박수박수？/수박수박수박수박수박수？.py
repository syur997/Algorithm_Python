def solution(n):
    odd = '수'
    even = '수박'
    if n == 1:
        return odd
    elif n % 2 == 0:
        return n // 2 * even
    else:
        return n // 2 * even + odd