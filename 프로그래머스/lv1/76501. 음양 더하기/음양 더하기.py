def solution(absolutes, signs):
    return sum(i*-1 if j == False else i for i,j in zip(absolutes, signs))