def anagrams(word, words):
    res = []
    for element in words:
        if (len(word) == len(element)) and (set(word) == set(element)):
            res.append(element)
    return res

test.assert_equals(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'])
test.assert_equals(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), ['carer', 'racer'])
