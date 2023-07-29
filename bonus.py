def string (letters:str) -> str:
    new=""
    if type(letters)==str:
         new=""
         for char in letters:
             if char.isupper():
                 new+=" "+char.lower()
             else :
                new+=char

         return new
    else:
        return " error type"

print(string("helloWorldThere"))