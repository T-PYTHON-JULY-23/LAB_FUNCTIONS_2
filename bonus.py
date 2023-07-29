def fix_str(sentance:str) -> str:
    '''this function will take string and return a string with a space befor every capital letter and but all the sentance in a lower case'''
    if type(sentance) == str:
        new_sent = ""
        for chr in sentance:
            if ord(chr) != ord(chr.lower()):
                new_sent += f" {chr.lower()}"
            else:
                new_sent += chr
        return new_sent
    else:
        return "error in parameter type"

print(fix_str("helloWorldThere"))
