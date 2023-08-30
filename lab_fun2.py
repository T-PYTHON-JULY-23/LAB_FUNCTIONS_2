def fined_primes (x,y):
   for number in range(x , y +1):
      for num in range(2 , number):
         if number%num ==0 :
            break
      else:
            print(number)
       
fined_primes(25,50) 
