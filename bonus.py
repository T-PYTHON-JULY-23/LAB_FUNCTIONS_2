
string_sentence=(input("What do you want to say?: "))


def str_checker(string_sentence:str):
    
    if type(string_sentence) == str:
        for i in string_sentence:
            for j in i:
                if i.isupper():
                 j = f" {i.lower()}"
            print(j,end="")
        
str_checker(string_sentence)

