a = [410,64,84,834,924,93,23,75,76,106]
print(a)
m = max(a)
n = min(a)
def difference(l):
    return max(l) - min(l)

print(f"The Difference b/w ({m} - {n}) is {difference(a)}")