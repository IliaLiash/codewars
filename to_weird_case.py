def to_weird_case(string):
    res = string.split()
    res_j = []
    for i in range(len(res)):
        s = ''
        for j in range(len(res[i])):
            if j % 2 == 0:
                s += res[i][j].upper()
            else:
                s += res[i][j].lower()
        res_j.append(s)
    return ' '.join(res_j)
