def title_case(title, minor_words=''):
    title = title.lower().split()
    minor_words = minor_words.lower().split()
    res = []
    try:
        for element in title:
            if element.lower() in minor_words:
                res.append(element.lower())
            else:
                res.append(element.title())
        res[0] = res[0].title()
    except:
        pass
    return ' '.join(res)
