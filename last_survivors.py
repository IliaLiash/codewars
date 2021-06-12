def last_survivors(string):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    while len(set(string)) != len(string):
        for element in string:
            if string.count(element) >= 2:
                string = string.replace(element, alpha[(alpha.index(element) + 1) % 26],1)
                string = string.replace(element,'',1)                
    return string
