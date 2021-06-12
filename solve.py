def solve(arr):
    res = []
    for element in arr[::-1]:
        if res.count(element) < 1:
            res.append(element)
    return res[::-1]
