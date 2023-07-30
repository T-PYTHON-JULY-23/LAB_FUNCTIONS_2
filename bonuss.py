def upto_low(word:str)-> str:
    upp=""
    if type(word) == str:
        upp= " "
        for ch in word:
            if ch.isupper():
                upp+=""+ch.lower()
            else:
                upp+= ch
                return upp
        else:
            return " not the type "
        print(upto_low("thieismyword"))

        
    