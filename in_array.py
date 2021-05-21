def in_array(array1, array2):
    print(array1)
    print(array2)
    res = []
    for string in array2:
        for substring in array1:
            if (substring in string) and (substring not in res):
                res.append(substring)
    res.sort()
    return res