def sum_dig_pow(a, b):
    res = []
    for element in range(a, b + 1):
        total = 0
        for j in range(len(str(element))):
            total += int(str(element)[j]) ** (j + 1)
        if total == element:
            res.append(total)
    return res
