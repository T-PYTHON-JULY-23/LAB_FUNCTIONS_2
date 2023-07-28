
#------------------lab --------------------------

def is_prime(num1):
    if num1 <= 1:  # يعني ان n اصغر من او تساوي 1
        return False
    for i in range(2, int(num1**0.5)+1): #معادلة الاعداد الاولية
        if num1 % i == 0: #باقي القسمة
            return False  #العدد غير اولي
    return True #العدد اولي

def find_primes(start, end):
    for num in range(start, end+1):
        if is_prime(num):
            print(num)


find_primes(25, 50)

#----------------------bonus---------------------------------------

def separate_words(string):
    if type(string) is not str:
        raise TypeError("")
    new_string = ""
    for char in string:
        if char.isupper():
            new_string += " " + char.lower()
        else:
            new_string += char
    return new_string.lower().strip()

print(separate_words("helloWorldThere"))