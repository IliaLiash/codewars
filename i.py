def i(word):
    if (len(word) == 0) or (word[0].islower()) or (word[0] in 'iI'):
        return 'Invalid word'
    vowels = 'aeiou'
    vowels_count = 0
    for sym in word:
        if sym.lower() in vowels:
            vowels_count += 1
    if vowels_count * 2 >= len(word):
        return 'Invalid word'
    return 'i' + word
