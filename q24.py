def basicallyDual(n, m):
  convertedM = sum(int(digit) * (n**count) for count, digit in enumerate(str(m)[::-1]))
  convertedN = sum(int(digit) * (m**count) for count, digit in enumerate(str(n)[::-1]))
  return convertedM == convertedN


totalmns = []

for ab in range(1,100):
  for pq in range(1,100):
    if basicallyDual(ab,pq) and ab != pq:
      totalmns.append(ab + pq)

print(max(totalmns))