
def number_between(number1:int  , number2:int ) -> None:
    for number_to_check in range(number1,number2):
        is_prime=True
        for i in range(2,number_to_check):
            if number_to_check%i==0:
                is_prime=False
                break       
        if is_prime:
            print(number_to_check)
        



number_between(25,50)