def anagrams(word, words):
    res = []
    for element in words:
        if (len(word) == len(element)) and (set(word) == set(element)):
            res.append(element)
    return res
