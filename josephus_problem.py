def josephus(n,k):
    #Your code here
    if n == 1:
        return 1
    return (josephus(n-1, k)+ k-1)%n + 1

print(josephus(3,2))