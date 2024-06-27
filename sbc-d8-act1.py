def read():
    users = {}
    try:
        with open("accounts.txt", "r") as file:
            for line in file:
                username, password = line.strip().split(",")
                users[username] = password
    except FileNotFoundError:
        pass
    return users

def write(users):
    with open("accounts.txt", "w") as file:
        for username, password in users.items():
            file.write(f" {username} , {password}\n")

def register(users):
    username = input("Enter Username: ")
    if username in users:
        print("Username already exists. Please try again.")
        return users
    password = input("Enter Password: ")
    users[username] = password
    write(users)
    print("Registration Successful!")
    return users

def login(users):
    username = input("Enter Your Username: ")
    if username not in users:
        print("Username not found. Please register first.")
        return
    password = input("Enter Your Password: ")
    if users[username] == password:
        print("Login Successful!")
    else:
        print("Incorrect password. Please try again.")

def change_password(users):
    username = input("Enter Your Username: ")
    if username not in users:
        print("Username not found. Please register first.")
        return users
    old_password = input("Enter your old password: ")
    if users[username] == old_password:
        new_password = input("Enter your new password: ")
        users[username] = new_password
        write(users)
        print("Password changed successfully!")
    else:
        print("Incorrect old password. Please try again.")
    return users

def exit(users):
    return 'exit'

def menu():
    users = read()
    actions = {
        'register': register,
        'login': login,
        'change_password': change_password,
        'exit': exit
    }

    while True:
        print("\nOptions: register, login, change_password, exit")
        choice = input("Choose an option: ").strip().lower()
        if choice in actions:
            result = actions[choice](users)
            if result == 'exit':
                print("Exiting the system.")
                break
            users = result if result else users
        else:
            print("Invalid option. Please try again.")

menu()
