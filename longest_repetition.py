def longest_repetition(chars):
    if len(chars) == 0:
        return ('', 0)
    
    chars = chars + ' '
    max_count = 0
    count = 1
    
    for i in range(len(chars) - 1):
        if chars[i] == chars[i + 1]:
            count += 1
        else:
            if count > max_count:
                char = chars[i]
                max_count = count
            count = 1
            
    return (char, max_count)
