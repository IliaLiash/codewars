def isPP(n):
    my_list = list(range(1, int(n**0.5) + 1))
    for element in my_list:
        for i in range(2, 20):
            if element ** i == n and i != 1:
                return [element, i]
                break
    return None
