def find_smallest_e():
  largest_e = 0

  es = []
  for a in range(1, 200):  # Adjust the range based on the problem constraints
      for b in range(a + 1, 300):
          for c in range(b + 1, 300):
              for d in range(c + 1, 300):
                  # Check if the triangles are similar
                  if a / b == b / c == c / d:
                      # Check the condition (d/a) < e
                      e = d / a
                      es.append(e)

  return es

result = find_smallest_e()
print(result)