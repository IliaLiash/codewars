def longest_palindrome(s):
    s = s + ' '
    res = ''
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i:j] == s[i:j][::-1] and len(s[i:j]) > len(res):
                res = s[i:j]
    return len(res)
