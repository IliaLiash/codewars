def stock_list(listOfArt, listOfCat):
    if listOfArt == []:
        return ''
    res = ''
    for cat in listOfCat:
        total = 0
        for art in listOfArt:
            if art.startswith(cat):
                total += int(art.split()[1])
        res += str(f'({cat} : {total}) - ')
    return res[:-3]
