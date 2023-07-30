def check_strings (string1:str):

    result = " "
    if type (string1) == str:
        print("the string entered is type of string ")
    else:
        print("Input must be a strin!")

    for char in string1 :
        if char.isupper():
            result += " " + char.lower() 
        else:
            result += char

    return result
   







print(check_strings("helloWorldThere"))










