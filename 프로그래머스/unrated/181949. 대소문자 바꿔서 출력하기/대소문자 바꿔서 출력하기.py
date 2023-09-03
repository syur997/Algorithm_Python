str = input()
x = []
for i in list(str):
    if i.islower():
        x.append(i.upper())
    else:
        x.append(i.lower())
print(''.join(x))