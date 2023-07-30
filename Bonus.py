def separate_words(s):
    if type(s) != str:
        return "Input must be a string"
    else:
        new_string = ""
        for letter in s:
            if letter.isupper():
               new_string += " "
            new_string += letter.lower()
        return new_string
    
print(separate_words("ILovePython"))