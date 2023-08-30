def separate_words (string : str) :
    if type(string) is not  str : # if not isinstance (tring , str)
         print (" it most be a string !")
    space = ""
    for i in (string): 
         if i.isupper() :
              space += " "+ i.lower() 
         else : 
             space +=i
    return space
example = "HelloWorldThere"
result = separate_words(example)
print (result)


