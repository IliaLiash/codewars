def solution(s):
    res = []
    for i in range(0, len(s), 2):
        if len(s[i:i+2]) < 2:
            res.append(s[i:i+2] + '_')
            break
        res.append(s[i:i+2])        
            
    return res
