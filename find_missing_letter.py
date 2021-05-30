def find_missing_letter(chars):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    chars = ''.join(chars)
    start = alphabet.find(chars[0].lower())
    for i in range(len(chars)):
        if chars[i].lower() != alphabet[start:][i].lower():
            return alphabet[start:][i] if chars.islower() else alphabet[start:][i].upper()
    
