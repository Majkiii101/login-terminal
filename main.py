import random
import sys

print("Welcome to my login terminal!")
print("Please choose 1 - register, 2 - login, 3 - exit")
choice = int(input("Your choice: "))
if choice == 1:
    print("Registering...")
    id = random.randint(1000, 9999)
    file = open(str(id)+'.txt', 'w')
    print("Your ID is: " + str(id) + ". Please remember it!" + "\n")
    password = input("Password: ")
    file.write(password)
    file.close()
    print("Registered successfully!")
elif choice == 2:
    print("Logging in...")
    print("Please enter your ID and password")
    id = int(input("ID: "))
    file = open(str(id)+'.txt', 'r')
    password = input("Password: ")
    if password == file.read():
        print("Logged in successfully!")
        file.close()
    else:
        print("Wrong password!")
elif choice == 3:
    print("Exiting...")
    sys.exit()


