def fact (n, res = 1):
    if n < 1:
        return res
    res = res * n
    return fact(n-1, res)

print(fact(4))