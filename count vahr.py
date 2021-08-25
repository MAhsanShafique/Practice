num = input("Enter character ")
total = ""
i = 0
while i < len(num):
    if num[i] not in total:
        total += num[i]
        print(f"#{num[i]} : {num.count(num[i])}")
    i += 1