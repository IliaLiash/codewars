def scramble(s1, s2):
    for i in range(100):
        try:
            if s2.count(s2[i]) > s1.count(s2[i]):
                return False
        except:
            pass
    return len(set(s2) - (set(s1) & set(s2))) == 0
  
#or from collections import Counter
