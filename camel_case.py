def camel_case(string):
    res = string.split()
    for i in range(len(res)):
        res[i] = res[i].title()
    return ''.join(res)
