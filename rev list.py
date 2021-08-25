i = list(range(1,11))

def Reversed_list(l):
    rev = []
    for a in range(len(l)):
        popped = l.pop()
        rev.append(popped)
    return rev
print(Reversed_list(i))
