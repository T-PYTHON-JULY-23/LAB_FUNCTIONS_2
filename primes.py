

def find_primes(frm:int, to:int):
    '''this function will ask for a range of numbers and will print all the prime numbers between those two numbers'''
    
    for i in range(frm + 1, to):
        #in this loop I want to check if the number is divisable by any number between 2 -> i-1 
        for j in range(2, i):
            if i % j == 0:
                break
            #here i want to make sure that the loop rotates completely
            elif j == i-1:
                print(i)


find_primes(25, 50)