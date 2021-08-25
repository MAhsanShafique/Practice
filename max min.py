def Max_Num(n,m):
    if n > m:
        return (f"Maximum num is {n}")

    return (f"Maximum num is {m}")

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
print(Max_Num(a,b))