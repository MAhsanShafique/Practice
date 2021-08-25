def fibonacci(f_name, l_name, age = 23):
    print(f"Ypur first name is {f_name}")
    print(f"Your last name is {l_name}")
    print(f"Your age is {age}")


F_name = input("Enter your first name: ")
L_name = input("Enter your last name: ")
Age = int(input("Enter your age: "))
fibonacci(F_name, L_name, Age)