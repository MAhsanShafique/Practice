def Even_Odd(l):
    even = []
    odd = []
    for i in l:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
        output = [odd , even]
    return output

lst = [1,2,3,4,5,6,7,8,9]
print(Even_Odd(lst))