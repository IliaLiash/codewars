import statistics

TOWNS = ["Rome", "London", "Paris", "NY", "Vancouver", "Sydney", "Bangkok", "Tokyo",
         "Beijing", "Lima", "Montevideo", "Caracas", "Madrid", "Berlin"]

def mean(town, strng):
    if town not in TOWNS:
        return -1
    strng = strng.split('\n')
    s = ''
    for element in strng:
        if town in element:
            for sym in element:
                if sym.isdigit() or sym in ' .':
                    s += sym
    res = [float(i) for i in s.split()]
    return statistics.mean(res) if len(res) > 0 else -1
    
def variance(town, strng):
    if town not in TOWNS:
        return -1
    strng = strng.split('\n')
    s = ''
    for element in strng:
        if town in element:
            for sym in element:
                if sym.isdigit() or sym in ' .':
                    s += sym
    res = [float(i) for i in s.split()]
    return statistics.pvariance(res) if len(res) > 0 else -1
