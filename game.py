w_num = 59
g_num = int(input("Enter the guess number b/t 1 & 100 "))
chance = 0
if g_num == w_num:
    print("You Win !!")
else:
    if g_num > w_num:
        print("too high!! ")
    else:
        print("too low!! ")