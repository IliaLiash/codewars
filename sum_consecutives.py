def sum_consecutives(s):
    s.append('')
    res = []
    mult = 1
    
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            mult += 1
        elif s[i] != s[i + 1]:
            res.append(mult * s[i])
            mult = 1
        else:
            res.append(s[i])
    return res
