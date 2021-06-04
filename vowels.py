VOWELS = '#aeiou'
def encode(st):
    s = ''
    for i in range(len(st)):
        if st[i].lower() in VOWELS:
            s += str(VOWELS.index(st[i]))
        else:
            s += st[i]
    return s
    
def decode(st):
    s = ''
    for i in range(len(st)):
        if st[i].isdigit():
            s += VOWELS[int(st[i])]
        else:
            s += st[i]
    return s
