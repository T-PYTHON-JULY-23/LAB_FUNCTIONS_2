
def SplitPhrases(text):
    if type(text) != str:
        return "Parameter must be a string"

    new_string = ""
    for i in range(len(text)):
        if text[i].isupper():
            new_string += " " + text[i].lower()
        else:
            new_string += text[i]

    return new_string

input_str = input("Enter an atached phrase: ")
output_str = SplitPhrases(input_str)
print(output_str)
