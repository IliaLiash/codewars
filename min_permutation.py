def min_permutation(n):
    if n == 0:
        return 0
    n_list = sorted([i for i in str(n) if i != '0' and i != '-'])
    print(n_list)
    if '0' not in str(n):
        return int(''.join(sorted(str(n))))
    else:
        res = []
        for i in range(len(str(n))):
            if str(n)[i] != '0' and str(n)[i] != '-':
                res.append(int(str(n)[i]))
        min_p = min(res)
    if str(n).startswith('-'):
        min_p = int('-' + str(min_p))
    zeros = str(n).count('0')
    return int(str(min_p) + '0'*zeros + ''.join(n_list[1:]))
