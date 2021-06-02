def goodVsEvil(good, evil):
    g = [1, 2, 3, 3, 4, 10]
    e = [1, 2, 2, 2, 3, 5, 10]
    good = [int(i) for i in good.split()]
    evil = [int(i) for i in evil.split()]
    
    for i in range(len(good)):
        good[i] = good[i] * g[i]
    for i in range(len(evil)):
        evil[i] = evil[i] * e[i]
    
    if sum(good) > sum(evil): 
        return 'Battle Result: Good triumphs over Evil'
    elif sum(good) < sum(evil):
        return 'Battle Result: Evil eradicates all trace of Good'
    else:
        return 'Battle Result: No victor on this battle field'
