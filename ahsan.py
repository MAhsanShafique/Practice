import random
w_num = random.randint(0,100)
g_num = int(input("Enter a number b/w 0 & 100: "))
attempt = 1
game_over = False
while not game_over:
    if g_num == w_num:
        print(f"You Win!!, You guess the number in {attempt} Attempts.")
        game_over = True
    elif g_num > w_num:
            print("Too High!!")
            attempt += 1
            g_num = int(input("Guess Again: "))
    else:
        print("Too Low !!")
        attempt += 1
        g_num = int(input("Guess Again: "))