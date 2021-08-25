def Greater(n,m):
    if n > m:
        return n
    else:
        return m

def Greatest(n,m,o):
    bigger = Greater(n,m)
    return Greater(bigger, c)


a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))
print(Greatest(a,b,c))