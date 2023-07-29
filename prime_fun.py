number1= int(input("please enter the first number: "))
number2 = int(input("please enter the second number: "))

print (f"The Prime Numbers in the range {number1} and {number2} are: ") 


def find_primes(number1:int,number2:int):

    for val in range(number1,number2+1):
        if val >1:
            for n in range(2,val):
                if (val % n == 0):
                    break
            else:
                print(val)


find_primes(number1,number2)
