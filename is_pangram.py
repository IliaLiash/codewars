import string

def is_pangram(s):
    rs = ''
    for i in range(len(s)):
        if s[i].isalpha and s[i] not in ' !,.!#':
            rs += s[i].lower()
    return len(set(rs)) >= 26
