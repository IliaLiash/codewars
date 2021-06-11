def square_digits(num):
    s = ''
    for i in range(len(str(num))):
        s += str(int(str(num)[i]) ** 2)
    return int(s)
