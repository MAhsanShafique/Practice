a = ['abc', 'mno', 'xyz']
def Rev_String(l):
    s = []
    for n in l:
        s.append(n[::-1])
    return s


print(Rev_String(a))