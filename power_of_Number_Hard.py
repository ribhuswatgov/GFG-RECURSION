def power(N,R):
    #Base case
    if N==0:
        return 0
    if R==0:
        return 1 #power is zero means answer is 1
    if R%2==0: #if R is even
        y=power(N,R/2) #finding r/2 power as power is even then storing answer in y and---
        y = (y * y) % 1000000007#---if power is even like 2^4 we can simply do (2^2)*(2^2)
    else:
            y = N % 1000000007 #If R is odd
            y = (y * power(N, R - 1) % 1000000007) % 1000000007
            ##--- reduce the power by 1 to make it even. The reducing power
            ##by one can be done if we take one n out. Like 2^3 can be written as 2*(2^2)
 
 
    return ((y + 1000000007) % 1000000007)# finally return the answer (y+mod)%mod = (y%mod+mod%mod)%mod = (y%mod)%mod

print(power(4,4))