def Separation(string:str):
    
    txt=isinstance(string,str)#check that the type of the parameter is of type str 
    if txt!=True:
       return "the argument is not string"
        
    else:
      result = ""
      for i in string:
        if i.isupper():
            result=result+" "+i.lower()#separates the word at any capital letter and replace it with a small letter
        else:
            result=result+i 
      return result# return the new modified string !

        
sentence="helloWorldThere"
        


print(Separation(sentence))