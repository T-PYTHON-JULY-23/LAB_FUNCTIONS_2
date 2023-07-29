
print("Welcome to finding primes between two numbers calculator!")

num1=int(input("Enter the first number: "))
num2=int(input("Enter the seconed number: "))

def find_primes(num1:int, num2:int):
      numbers_range = range(num1,num2)
      for i in numbers_range: 
          if i > 1: 
            for number in range(2,i): 
             if (i% number) == 0:
                 break 
            else:
             print(i)
               
print(f"primes between {num1} and {num2} are:")
find_primes(num1,num2)