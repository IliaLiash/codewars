import math

def is_prime(num):
    if num == 1 or num == 0 or num < 1:
        return False
    count = 0
    for i in range(1, int(abs(num)**0.5) + 1):
        if num % i == 0:
            count += 1
            if count > 1:
                return False
    return True
