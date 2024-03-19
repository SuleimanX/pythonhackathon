def fibonacci(n):

  if n <= 1:
    return[0]
    
  else:
    a, b = 0, 1
    for _ in range(2, n + 1):
      c = a + b
      fibonacci_sequence.append (c)
      a, b = b, c
    return fibonacci_sequence

# Get the number of terms from the user
num_terms = int(input("Enter the number of terms: "))

# Generate the Fibonacci sequence
fibonacci_sequence = []
for i in range(num_terms):
  fibonacci_sequence.append(fibonacci(i))

# Print the Fibonacci sequence
print(fibonacci_sequence)

fibonacci(num_terms)
