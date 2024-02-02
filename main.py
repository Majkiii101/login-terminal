import os.path
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
        if os.path.exists(str(id)+'.txt'): # checks if the file with the name of the generated id exists
            id = random.randint(1000, 9999)
            if os.path.exists(str(id)+'.txt'):
                print("Sorry, we couldn't generate an ID for you. Please try again later.")
                sys.exit()
        file = open(str(id)+'.txt', 'w') # creates a file with the name of the generated id
        print("Your ID is: " + str(id) + ". Please remember it!" + "\n")
        password = input("Password: ")
        while(len(password) <= 8): # checks if the password is less than 8 characters
            print("Password must be at least 8 characters long!")
            password = input("Password: ")
        file.write(password) # writes the password to the file
        file.close()
        print("Registered successfully!")
    elif choice == 2: # if the user chooses 2, the program will log them in
        print("Logging in...")
        print("Please enter your ID and password")
        id = int(input("ID: "))
        file = open(str(id)+'.txt', 'r') # opens the file with the name of the id
        chances = 3  # sets the chances to 3 so the user can try 3 times
        password = input("Password: ")
        while(password != file.read()): # reads the file and checks if the password is correct
            chances -= 1
            print("Wrong password! You have " + str(chances) + " chances left.")
            if chances == 0:
                print("You've guessed wrong to many times. Exiting...")
                sys.exit()
            file.seek(0) # sets the file's cursor to the beginning of the file
            password = input("Password: ")
        print("Logged in successfully!")
        file.close()
    elif choice == 3: # if the user chooses 3, the program will exit
        print("Exiting...")
        sys.exit() # exits the program
    else:
        print("Invalid choice!")




