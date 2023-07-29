def find_primes(num1: int, num2: int) :
#Prints the prime numbers 
    for num in range(num1, num2+1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)
find_primes(25, 50)       