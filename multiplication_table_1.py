def multiplication_table(row,col):
    res = []
    for i in range(1, row+1):
        r = []
        for j in range(1, col+1):
            r.append(i*j)
        res.append(r)
    return res
