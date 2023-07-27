"""# Bonus
## write a function that takes a string as a parameter
- first check that the type of the parameter is of type str
- then, it should separates the word at any capital letter and replace it with a small letter 
- and  should return the new modified string !

Example: `helloWorldThere` should return :
```hello world there```
"""
def upper_to_loower(phrase:str) -> str:
    if type(phrase)!=str:
        return "Not string "
    
    full_phrase=""
    for char in phrase:
        if char.isupper():
            full_phrase+=" "+char.lower()
        else :
            full_phrase+=char
    
    return full_phrase

phrase="helloWorldThere"
phrase_with_spaces=upper_to_loower(phrase)
print(phrase_with_spaces)
        
        



