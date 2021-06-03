from collections import Counter

def letter_frequency(text):
    s = ''
    for element in text:
        if element.isalpha():
            s += element.lower()
    return sorted(Counter(s).items(), key=lambda x: (-x[1], x[0]))
