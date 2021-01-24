def max_pieces(n, a, b, c):

    if n == 0:
        return 0
    if n<0:
        return -1
    res1 = max_pieces(n-a, a,b,c)
    res2 = max_pieces(n-b, a,b,c)
    res3 = max_pieces(n-c, a,b,c)

    res_final = max(res1, res2, res3)

    if res_final == -1:
        return -1
    return res_final+1

print(max_pieces(5,2,5,1)) 


    