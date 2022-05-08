from factorial import Factorial

f = Factorial()

def factorial(n):
  if n == 0:  
    return 1  
  else:
    return(n * factorial(n-1))

n = 200

for i in range(1000000):
    f.factorial(n)
    #factorial(n)
