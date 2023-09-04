def solution(array):
    count = {}
    for i in array:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    max_value = max(count.values())
    max_list = [key for key, value in count.items() if value == max_value]
    
    if len(max_list) == 1:
        return max_list[0]
    else:
        return -1