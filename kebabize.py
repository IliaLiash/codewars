def kebabize(string):
    s = ''
    for element in string:
        if element.isupper():
            s += '-' + element.lower()
        elif element.isdigit():
            continue
        else:
            s += element
    return s.strip('-')
