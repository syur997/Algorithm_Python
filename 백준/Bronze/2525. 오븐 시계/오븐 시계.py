x, y = map(int, input().split())
z = int(input())

if y + z >= 60 :
  i = (y + z) % 60
  x += (y + z) // 60
  if x >= 24 :
    x -= 24
  print(x, i)
else :
  print(x, y + z)