import math, numpy

def f(num): 
  return math.ceil(math.floor(math.ceil(math.floor(num)+num**2)+num**3)+num**4)

for i in numpy.arange(0,2,0.001):
  print(f(i))