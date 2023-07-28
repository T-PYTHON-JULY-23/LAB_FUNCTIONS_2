

def prim_number (num1:int, num2:int):
    for i in range(num1 , num2+1):
        if i > 1:
            for j in range(2, i):
                if ( i%j )==0:
                    break
            else:
                print (f"primes numbers between {num1} and {num2} are: {i}" )
               

prim_number(25, 50)

    
























