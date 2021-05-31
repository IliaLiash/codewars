def find_outlier(integers):
    even = 0
    for i in range(len(integers)):
        if integers[i] % 2 == 0:
            even += 1
    if even > 1:
        return [i for i in integers if i % 2 != 0][0]
    else:
        return [i for i in integers if i % 2 == 0][0]
