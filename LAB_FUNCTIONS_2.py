def prime_number(num1:int ,num2:int):
    print(f"The prime numbers are : ")
    for num in range(num1,num2+1):
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    break
            else:
                print(num)

prime_number(25,50)