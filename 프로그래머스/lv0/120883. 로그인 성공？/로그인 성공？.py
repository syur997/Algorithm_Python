def solution(id_pw, db):
    x = ''
    for i in db:
        if id_pw[0] == i[0] and id_pw[1] == i[1]:
            x = 'login'
            break
        elif id_pw[0] == i[0] and id_pw[1] != i[1]:
            x = 'wrong pw'
            break
        elif id_pw[0] != i[0] and id_pw[1] == i[1]:
            x = 'fail'
    return x