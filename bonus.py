def hello_world(text:str):
    if type(text) == str:
        print("Your variable is string")
    else:
      print('Your variable is not string')
    split=""
    for i in range(len(text)):
        if (text[i].isupper()):
            split+= " "
            split+= text[i]
        else:
            split += text[i]
    return split.lower()
print(hello_world("helloWorldThere"))

