
def find_primes(num:int = 50, num2:int = 25):  
    ''' to find primes numbers between the first parameter and the second parameter and print it'''   
    for number in range(num2,num+1):
        for numberTest in range(2,num+1):
            if number%numberTest == 0:
                break
        if number == numberTest:
            print(number)
find_primes()
print('-'*20)
find_primes(70,20)