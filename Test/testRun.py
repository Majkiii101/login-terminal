import os.path
import random
import sys
import hashlib

def register():
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
    while len(password) < 8 or password is None: # checks if the password is less than 8 characters
        print("Password must be at least 8 characters long and cannot be empty!")
        password = input("Password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest() # hashes the password
    file.write(hashed_password) # writes the password to the file
    file.close()
    print("Registered successfully!")

def logedIn():
    print("Logged in successfully! You can now use the terminal. Type 'exit' to log out.")
    word = input("Say something to the terminal: ")
    print("You've said " + word)
    while word != "exit":
        word = input("Say something else!:")
        if word == "exit":
            print("Logging out...")
            break
        print("You've said: " + word)

def login():
    print("Logging in...")
    print("Please enter your ID and password")
    id = None
    while id is None:
        try:
            id = int(input("ID: "))
        except ValueError:
            print("Invalid ID!")
    file = open(str(id)+'.txt', 'r') # opens the file with the name of the id
    chances = 3  # sets the chances to 3 so the user can try 3 times
    stored_hashed_passwword = file.read().strip() # reads the file and stores the hashed password
    file.close()
    password = input("Password: ")
    while hashlib.sha256(password.encode()).hexdigest() != stored_hashed_passwword: # reads the file and checks if the password is correct
        chances -= 1
        print("Wrong password! You have " + str(chances) + " chances left.")
        if chances == 0:
            print("You've guessed wrong to many times. Exiting...")
            sys.exit()
        password = input("Password: ")
    file.close()
    isLoggedIn = True
    while isLoggedIn: # if the user is logged in, the program will call the logedIn function
        logedIn()
        isLoggedIn = False # sets the isLoggedin to False so the program can exit the while loop

print("Welcome to my login terminal!")
choice = 0 # sets the choice to 0 so the while loop can run
while choice != 3:
    print("Please choose 1 - register, 2 - login, 3 - exit")
    choice = int(input("Your choice: "))  # simple input that takes the user's choice
    if choice == 1: # if the user chooses 1, the program will register them
        register()
    elif choice == 2: # if the user chooses 2, the program will log them in
        login()
    elif choice == 3: # if the user chooses 3, the program will exit
        print("Exiting...")
    else:
        print("Invalid choice!")
