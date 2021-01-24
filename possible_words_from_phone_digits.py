mapping = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
def possibleWords(a,N):
    
    possible_Strings(a, 0, N, [])
    
def possible_Strings(a, curr, N, output):
    
    if curr == N:
        new_string= "".join(output)
        print(new_string,end=" ")
        return
    
    for index in range(0, len(mapping[a[curr]])):
        output.append(mapping[a[curr]][index])
        possible_Strings(a, curr+1, N, output)
        output.pop()

possibleWords([2,3,4], 3)