def find_the_primeNum(num1:int , num2: int):
    for i in range(num1,num2+1):
        for j in range (2,num1+1):
            if i%j== 0:
                break
            if i == j:
                print(i)
                find_the_primeNum
                find_the_primeNum(25,50)
    