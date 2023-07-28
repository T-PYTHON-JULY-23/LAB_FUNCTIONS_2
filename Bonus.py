def check_strings (string1:str):

    result = " "
    if type (string1) == str:
        print("the string entered is type of string ")
    else:
        print("Input must be a strin!")

    for char in string1 :
        if char.isupper():
            result += " " + char  
        else:
            result += char

    return result.lower()
   







print(check_strings("helloWorldThere"))











'''

            for i in string1:
                if (i.isupper())== True:
                    result+=(i.lower())
                    '''



'''
    for char in string1 :
        if char.isupper():
            result += " " + char  
        else:
            result += char
            
    return result.split()
'''
'''
    for char in string1 :
        if char.isupper():
            result += " " + char 
        else:
            result += char
'''
'''
        for i in string1:
            if (i.isupper())== True:
                result+=(i.lower()) '''