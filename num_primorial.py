from functools import reduce

def num_primorial(n):
    res = []
    for i in range(2, n**2):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            res.append(i)
            if len(res) == n:
                break
            
    return reduce(lambda x, y: x*y, res)
