'''
Try using modulus property with fast exponentian:

Property 1:
(m * n) % p has a very interesting property:
(m * n) % p =((m % p) * (n % p)) % p

Property 2:
if b is even:
(a ^ b) % c = ((a ^ b/2) * (a ^ b/2))%c ? this suggests divide and conquer
if b is odd:
(a ^ b) % c = (a * (a ^( b-1))%c

Property 3:
If we have to return the mod of a negative number x whose absolute value is less than y:
then (x + y) % y will do the trick

Note:
Also as the product of (a ^ b/2) * (a ^ b/2) and a * (a ^( b-1) may cause overflow, 
hence we must be careful about those scenarios
'''
def power(N,R):
    #Your code here

    if(R==1):
        return N
    if(R==0):
        return 1
    
    if R%2 == 0:

        res = ((power(N,R/2)%1000000007)*(power(N,R/2)%1000000007))%1000000007

        if res < 0:
            res = int((res + 1000000007)%1000000007)

    else:
        res = (N*power(N,R-1))%1000000007
        
        if res < 0:
            res = int((res + 1000000007)%1000000007)
    
    return res

print(power(4,4))