num = input("Enter numbers to add ")
total = 0
i = 0
while i < len(num):
    total = total + int(num[i])
    i += 1
print(total)