from itertools import combinations

def choose_best_sum(t, k, ls):
    towns_comb = list(combinations(ls, k))
    max_towns_dist = 0
    res = []
    
    for towns in towns_comb:
        if sum(towns) == t:
            return sum(towns)
        elif max_towns_dist < sum(towns) < t:
            res = towns
            max_towns_dist = sum(towns)
        
    return sum(res) or None
