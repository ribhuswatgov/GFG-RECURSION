def fib(n):
    if n%2==0:
        c = prime(n/2)
        return c


    else:
        if n == 1:
            return 1
        if n == 3:
            return 1
        return fib(n-2) + fib(n-4)

def prime(n):
    f=2
    s = 1

    while s!=n:
        result = isPrime(f)
        if result is True:
            s = s+1
            prime_number = f
            f = f+1
        else:
            f = f+1

    return prime_number

def isPrime(n):
    if n ==2:
        return True
    for index in range(2, n):
        if n% index == 0:
            return False
        return True

print(fib(14))


