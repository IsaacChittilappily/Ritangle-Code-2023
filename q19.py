u1, u2, n, golden = 12**3, 45**6, 1, (1 + (5 ** 0.5)) / 2

print(((78**9)/5))

while n != 78**9:
  
  n += 1
  u3 = (golden * u2) - u1
  
  u1 = u2
  u2 = u3
  print(u1)