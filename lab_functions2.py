def prime(number1, number2 ):
    
    print(f"primes between {number1} and {number2} are:")
    for i in range(number1, number2 ):
                for j in range(2 , i):  
                    if (i % j) == 0:
                        break
                else:

                    print(i)

prime(25,50)
