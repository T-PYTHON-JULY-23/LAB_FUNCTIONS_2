def fix_str(sentance:str) -> str:
    '''this function will take string and return a string with a space befor every capital letter and but all the sentance in a lower case'''
    if type(sentance) == str:
        new_sent = ""
        for chr in sentance:
            '''
            every letter or sympol have a Unicode, 
            Unicode is simply a number to represante a letter or sympol, 
            here i want to compare the later in it's original case and the lower case
            if they are not equale then the letter is in the upper case i have to add 
            space befor the letter and change the case of the letter to be lower case 
            if not the i just need append it normaly.
            for example :
            ord("W") != ord("w") will return True.
            '''
            if ord(chr) != ord(chr.lower()):
                new_sent += f" {chr.lower()}"
            else:
                new_sent += chr
        return new_sent
    else:
        return "error in parameter type"

print(fix_str("helloWorldThere"))
