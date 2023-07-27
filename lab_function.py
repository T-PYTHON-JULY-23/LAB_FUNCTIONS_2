
def is_prime(number):
  for i in range(2,number):
    if (number%i) == 0:
      return False
  return True

def find_primes(num1,num2):
    for number in range(num1,num2+1):
        if is_prime(number)==True:
            print(number)

find_primes(25,50)
        
        
