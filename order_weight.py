def order_weight(strng):
    my_list = sorted(list(map(str,strng.split())))
    
    return ' '.join(sorted(my_list, key = lambda x: (sum([int(i) for i in x]))))
