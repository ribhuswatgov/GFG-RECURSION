def subset(word, ls= [], index = 0):
    if index == len(word):
        return ls
    
    subset(word, ls = ls.append(word[:index]), index+1)
    subset(word, ls = ls.append(word[:index+1]), index+1)

ls = []  
print(subset("ABC", ls))
