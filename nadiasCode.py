username = "nadia"
password = "fanta"
running = True
while running:
    name = input("Enter your name")
    pwd = input("Enter your password")
    if name == username and pwd == password:
        print("Your details are correct")
        running = False
    else:
        print("Your details are not correct, please try again")
