#functions
Num1 = int(input("enter the first number: "))
Num2 = int(input("enter the second number: "))

def find_primes(Num1, Num2):

    for i in range(Num1, Num2+1):
        count = 0
        for j in range(1, i+1):
            if (i % j)==0:
                count=count+1
        if count==2:
            print(i)

find_primes(Num1, Num2)
