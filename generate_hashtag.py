def generate_hashtag(s):
    if len(s) == 0 or len(s) > 140:
        return False
    s = s.split()
    for i in range(len(s)):
        s[i] = s[i].capitalize()
    return '#' + ''.join(s)