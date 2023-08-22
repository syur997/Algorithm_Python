def solution(my_string, index_list):
    x = ''
    for i in index_list:
        x += my_string[i]
    return x