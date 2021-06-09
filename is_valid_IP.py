def is_valid_IP(strng):
    if len(strng.split('.')) != 4 or len(strng) == 0:
        return False
    for element in strng.split('.'):
        for i in range(len(element)):
            if element[i].isalpha():
                return False
        if int(element) > 255:
            return False
        if (element.startswith('0') and len(element) == 3) or element.startswith('-'):
            return False
        if ' ' in element:
            return False
    return True
