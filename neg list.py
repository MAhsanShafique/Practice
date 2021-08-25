i = list(range(1,6))
t = 0
def square(l):
    Sq = []
    for s in l:
        Sq.append(s**2) #s*s is also true
    return Sq

print(square(i))