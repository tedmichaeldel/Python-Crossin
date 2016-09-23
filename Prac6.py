def Fibonacci(n):
    a = 1
    b = 1
    print a
    print b
    for i in range(3,n+1):
        c = a + b
        print c
        a = b
        b = c

Fibonacci(7)