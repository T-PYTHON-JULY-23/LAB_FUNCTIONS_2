
#prime Numbers
def find_prime(start,end):
    for number in range(start, end + 1):
        if number > 1:
         for i in range(2, number):
           if (number % i) == 0:
               break
         else:
           print(number)

find_prime(25,50)
