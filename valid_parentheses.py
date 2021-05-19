def valid_parentheses(string):
    total = 0
    flag = True
    for element in string:
        if total < 0:
            return False
        elif element == '(':
            total += 1
        elif element == ')':
            total -= 1
    return flag if total == 0 else False