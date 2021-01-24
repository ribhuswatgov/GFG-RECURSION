def RecursivePower(n,p):

    if p == 1:
        return n
    return n * RecursivePower(n,p-1)

print(RecursivePower(2,9))