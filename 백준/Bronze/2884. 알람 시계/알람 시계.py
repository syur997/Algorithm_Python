H, M = map(int, input().split())

if M >= 45 :
  M -= 45
  print(H, M)
elif H == 0 :
  H = 24
  H -= 1
  M += 15
  print(H, M)
else :
  H -= 1
  M += 15
  print(H, M)