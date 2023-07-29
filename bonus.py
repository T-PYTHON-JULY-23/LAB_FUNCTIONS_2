def split_uppercase(string):
    result = ""

    for char in string:
        if char.isupper():
            result += " " + char.lower()

        else:
            result += char

    return result


def type_check(char_type):
    if char_type.isdigit():
        int(char_type)
        print("plese enter string value only")
    else:
        print(split_uppercase(sentence_value))


sentence_value = input("Enter your sentence :")
type_check(sentence_value)
