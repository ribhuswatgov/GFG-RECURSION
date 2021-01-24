def permutation_of_String(s, l, r):
    new_list= []
    if l == r:
        print(s)
    for index in range(l,r+1):
        ls = list(s)
        ls[l],ls[index] = ls[index],ls[l]
        new_string = "".join(ls)
        new_list.append(new_string)
    
    for index in new_list:
        permutation_of_String(index,l+1,r)
    
permutation_of_String("ABC", 0, 2)