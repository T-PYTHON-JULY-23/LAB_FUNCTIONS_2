



def prime(number1,number2):
        for num in range(number1, number2+1):
            if num>1:
                 for i in range(2,num):
                   if num%i == 0:
                        break
                   else:
                    print(num)
            
                




print("Enter two number to print all prime numbers in between of")

inputUser1=int(input("First Number: "))
inputUser2=int(input("Second Number: "))


prime(inputUser1,inputUser2)