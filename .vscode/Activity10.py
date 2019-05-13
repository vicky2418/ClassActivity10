input_string = input("Enter your student number separated by space ")
list  = input_string.split()
print("The student number is: " , list)


#num = int (input("Enter your student number: "))
#print("The student number is: ", num)

def checkPrime(list):
  p = 0
  for x in range (0, len(list)):
    num = list[x]
    if num > 1:
      prime = True
      for j in range(2, int(num**0.5)+1):
          if num%j == 0:
              prime = False
              break
      if prime:
        p = p + num
        print("The number of prime numbers is: ", p)

checkPrime(p)


from random import *

q = randint(25, 50)    
print("The random number is: " , q)

import math
def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier

r = int(round_down(q / p))
print("The number of strings to be generated is: ", r)


import random
import string

for x in range(r):
  def randomString(stringLength=5):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


  print(randomString(5))
  print(randomString(7))

