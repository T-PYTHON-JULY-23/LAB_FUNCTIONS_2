def modified_string(sentence:str):
    if isinstance(sentence,str) == False :
        return 'sorry try again by enter a string sentence'
    else:
        newSentence = sentence.lower()
        return newSentence
print(modified_string(56))
print('-'*20)
print(modified_string('helloWorldThere'))