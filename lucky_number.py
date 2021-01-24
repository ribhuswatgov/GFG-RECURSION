''' Lucky numbers are subset of integers. 
Rather than going into much theory, let us see the process of arriving at lucky numbers,

Take the set of integers
1,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,18,19,……

First, delete every second number, we get following reduced set.
1,3,5,7,9,11,13,15,17,19,…………

Now, delete every third number, we get
1, 3, 7, 9, 13, 15, 19,….….

Continue this process indefinitely……
Any number that does NOT get deleted due to above process is called “lucky”.

Your task is to complete isLucky function.

Input Format: The first line of input contains an integer T denoting the number of test cases. 
Then T test cases follow. The first line of each test case contains an integer N. 

Output Format: For each testcase, in a new line, print 1 if the given number is a lucky number, else print 0.

Your Task:
This is a function problem. 
You only need to complete the function isLucky that takes n as parameter and returns either 0 or 1.

'''
# Asked At Microsoft
def isLucky(n):
    
    return lucky(n,2)

def lucky(n,c):
    
    if n%c==0:
        return 0
    
    if c>n:
        return 1
    
    n = n - int(n/c)
    
    return lucky(n,c+1)

print(isLucky(5))