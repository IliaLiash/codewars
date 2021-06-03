from collections import Counter

def added_char(s1, s2):
    a = Counter(s1)
    b = Counter(s2)
    return list(set(b.items()) - set(a.items()))[0][0]    
