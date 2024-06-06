import itertools

# package to generate all permutations of an array

permutations = list(itertools.permutations([1, 2, 3, 4, 5, 6, 7, 8]))
# creates a list of all permutations

valid, invalid = 0,0

for x in permutations:
  
  a,b,c,d,e,f,g,h = x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7]
  
  if a*b*c*d*e < f*g*h: # if the condition is met, add 1 to successful permutations
    valid+=1
    
  else: # otherwise, add 1 to unsuccessful attempts
    invalid += 1

print(valid/(valid+invalid)) # prints the probability