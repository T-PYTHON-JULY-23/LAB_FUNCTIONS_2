def fined_primes (x,y):
    for check_number in range(x,y) :
        if check_number % 2 == 0 :
            continue
        else :
            print (f"{check_number}")
       

fined_primes(29,50) 
