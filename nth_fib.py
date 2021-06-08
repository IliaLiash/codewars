def nth_fib(n):
    if n == 1:
        return 0
    a = 0
    b = 1
    for _ in range(1,n):
        a, b = b, a + b
    return a
