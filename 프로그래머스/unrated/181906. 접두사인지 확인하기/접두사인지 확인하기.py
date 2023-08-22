def solution(my_string, is_prefix):
    for i in range(len(is_prefix)+1):
        if my_string[:i] == is_prefix:
            return 1
        else:
            pass
    return 0