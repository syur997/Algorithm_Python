def solution(array, commands) :
    x = []
    for i in range(len(commands)) :
        x.append(sorted(array[commands[i][0]-1:commands[i][1]])[commands[i][2]-1])
    return x