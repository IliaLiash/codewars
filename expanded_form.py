def expanded_form(num):
    s = ''
    tens = 1
    
    while num != 0:
        new_num = num % 10 * tens
        num = num // 10
        tens *= 10
        if new_num != 0:
            s += f'{new_num} '
        
    return ' + '.join(s.split()[::-1])
