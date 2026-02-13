def tm(A, C, G, T):
    length = A + C + G + T
    if length == 0:
        return None

    if length <= 13:
        return (A + T) * 2 + (G + C) * 4
    
    return 64.9 + 41 * (G + C - 16.4) / length


print(tm(5, 7, 3, 4))   
print(tm(3, 3, 3, 3))  
print(tm(10, 0, 10, 0)) 
