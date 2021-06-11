def find_short(s):
    return len(sorted([word for word in s.split()], key = len)[0])
