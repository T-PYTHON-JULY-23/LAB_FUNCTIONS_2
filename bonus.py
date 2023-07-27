# helloWorldThere
def space_letter(name) -> str:
    ''' Space Between cabital letters'''
    res=""
    for i in name:
        if i.isupper():
            res = res+" "+i.upper()
        else:
            res=res+i
    return res
print(space_letter("helloWorldThere"))