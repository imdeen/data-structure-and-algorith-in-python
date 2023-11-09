#recursive
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    


#iterative
def fibo(n):
    t0 = 0
    t1 = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    for i in range(2, n+1):
        s = t0 + t1
        t0 = t1
        t1 = s
    return s
print(fibo(7))