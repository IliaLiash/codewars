def solution(number):
    total = 0
    for i in range(number):
        if (i % 5 == 0) and (i % 3 == 0):
            total += i
        elif i % 5 == 0:
            total += i
        elif i % 3 == 0:
            total += i
    return total