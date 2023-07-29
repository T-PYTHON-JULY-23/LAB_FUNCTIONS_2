def hello_world(text:str):
    if type(text) == str:
        print("your variable is string")
    else:
      print('your variable is not string')
    spliter=""
    for i in range(len(text)):
        if (text[i].isupper()):
            spliter += " "
            spliter += text[i]
        else:
            spliter += text[i]
    return spliter.lower()
print(hello_world("helloWorldThere"))

