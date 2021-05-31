def high(x):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    x = x.split()
    res = []
    for i in range(len(x)):
        total = 0
        for j in range(len(x[i])):
            total += alphabet.index(x[i][j]) + 1
        res.append(total)
    return x[res.index(max(res))]
