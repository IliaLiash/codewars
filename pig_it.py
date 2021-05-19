def pig_it(text):
    words = text.split()
    res = []
    for word in words:
        if ('!' not in word) and ('?' not in word):
            word = word + ' '
            word = word.replace(word[-1], word[0])
            word = word[1:] + 'ay'
        res.append(word)
    return ' '.join(res)