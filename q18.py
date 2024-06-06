sums = {9999999}

for a in range(2,100):
  for b in range(a+1,100):
    for c in range(b+1,100):
      for d in range(c+1,100):
        for e in range(d+1,100):
          if round(1/e - 1/d,2) == round(1/d - 1/c,2) == round(1/c - 1/b,2) == round(1/b - 1/a,2):
            sums.add(a+b+c+d+e)
            print(min(sums))
            
print('The min number is' + str(min(sums)))