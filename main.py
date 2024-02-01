import random
import sys

print("Welcome to my login terminal!")
choice = 0 # sets the choice to 0 so the while loop can run
while(choice != 3):
    print("Please choose 1 - register, 2 - login, 3 - exit")
    choice = int(input("Your choice: "))  # simple input that takes the user's choice
    if choice == 1: # if the user chooses 1, the program will register them
        print("Registering...")
        id = random.randint(1000, 9999) # generates a random 4 digit number
        file = open(str(id)+'.txt', 'w') # creates a file with the name of the generated id
        print("Your ID is: " + str(id) + ". Please remember it!" + "\n")
        password = input("Password: ")
        file.write(password) # writes the password to the file
        file.close()
        print("Registered successfully!")
    elif choice == 2: # if the user chooses 2, the program will log them in
        print("Logging in...")
        print("Please enter your ID and password")
        id = int(input("ID: "))
        file = open(str(id)+'.txt', 'r') # opens the file with the name of the id
        password = input("Password: ")
        if password == file.read(): # reads the file and checks if the password is correct
            print("Logged in successfully!")
            file.close()
        else:
            print("Wrong password!")
    elif choice == 3: # if the user chooses 3, the program will exit
        print("Exiting...")
        sys.exit() # exits the program


