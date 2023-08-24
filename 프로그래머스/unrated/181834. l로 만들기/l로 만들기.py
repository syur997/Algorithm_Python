def solution(myString):
    x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    for i in myString:
        if i in x:
            myString = myString.replace(i, 'l')
    return myString