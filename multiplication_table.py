def multiplication_table(size):
    res = []
    for i in range(1, size + 1):
        row = []
        for j in range(1, size + 1):
            row.append(i * j)
            if len(row) == 3:
                res.append(row)
    return res
