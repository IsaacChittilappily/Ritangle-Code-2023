from functools import reduce


def factors(n):
    return set(reduce(list.__add__,
                      ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))


listD = []

for m in range(1, 500):
    for n in range(1, 500):
        if len(list(factors(m))) == len(list(factors(n))) == 6:
            listD.append(len(list(factors(m * n))))

print(listD := sorted(dict.fromkeys(listD)))

totalD = sum(listD)
print(totalD)