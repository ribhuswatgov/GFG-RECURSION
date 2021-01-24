def sum_of_digits(n):
    if int(n/10) == 0:
        return n%10
    
    rem = n%10
    return rem + sum_of_digits(int(n/10))

print(sum_of_digits(253))