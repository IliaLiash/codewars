def to_nato(words):
    s = ''
    for i in range(len(words)):
        if words[i].lower() in 'abcdefghijklmnopqrstuvwxyz':
            s += NATO[words[i].upper()] + ' '
        elif words[i] == ' ':
            continue
        else:
            s += words[i] + ' '
    s = s.replace('  ',' ')
    return s.strip()
