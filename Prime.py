# FirstNum = int(input("Enter first Number:"))
# SecNum = int(input("Enter second Number:"))
def prime(FirstNum,SecNum):
    for num in range(FirstNum,SecNum + 1):
        if num > 1:
            for i in range(2 , num):
                if (num % i ) == 0:
                    break
            else:
                print(num)
prime(25,50)