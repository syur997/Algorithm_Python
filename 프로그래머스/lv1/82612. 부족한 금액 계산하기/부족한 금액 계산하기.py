def solution(price, money, count):
    total_price = sum(price * i for i in range(1, count+1))
    change = total_price - money
    if change > 0:
        return change
    else:
        return 0