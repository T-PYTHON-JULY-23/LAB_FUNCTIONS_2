def separate_words (string : str) :
    if type(string) != str :
         print (" it most be a string !")
    space = ""
    for i in (string): 
         if i.upper() :
              space += " "+ i.lower() 
         else : 
             space +=i
    return space
example = "helloWorldThere"
result = separate_words(example)
print (result)


