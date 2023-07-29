

def find_primes(x, y):
    for num in range(x, y):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)


find_primes(int(input("enter the lower number ")),
            int(input("enter the upper number ")))
