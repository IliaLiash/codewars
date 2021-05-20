def order(sentence):
    res = sentence.split()
    sentence = sentence.split()
    for element in sentence:
        for k in range(len(element)):
            if element[k].isdigit():
                res[int(element[k])-1] = element
                break
    return ' '.join(res)