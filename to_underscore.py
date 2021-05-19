def to_underscore(string):
    string = str(string)
    s = string[0].lower()
    for i in range(1, len(string)):
        if string[i].isupper():
            s += '_' + string[i].lower()
        else:
            s += string[i]
    return s