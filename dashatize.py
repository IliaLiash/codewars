def dashatize(n):
    if n is None:
        return 'None'
    n = abs(n)
    s = ''
    for i in range(len(str(n))):
        if int(str(n)[i]) % 2 == 1:
            s += f'-{str(n)[i]}-'
        else:
            s += str(n)[i]
    return s.replace('--','-').lstrip('-').rstrip('-')
