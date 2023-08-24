def solution(names):
    return [names[i] for i in range(len(names)) if i == 0 or i % 5 == 0]