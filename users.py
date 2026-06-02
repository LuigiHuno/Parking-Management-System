from data import *


users = load_data(USERS_FILE)



if len(users) == 0:

    users.append({
        "username": "admin",
        "password": "admin123",
        "role": "admin"
    })

    users.append({
        "username": "owner",
        "password": "owner123",
        "role": "owner"
    })

    save_data(USERS_FILE, users)



def register_customer():

    print("\n===== CUSTOMER REGISTRATION =====")

    username = input("Enter username: ")
    password = input("Enter password: ")

    for user in users:

        if user["username"] == username:
            print("Username already exists!")
            return

    new_user = {
        "username": username,
        "password": password,
        "role": "customer"
    }

    users.append(new_user)

    save_data(USERS_FILE, users)

    print("Registration successful!")



def login(role):

    print(f"\n===== {role.upper()} LOGIN =====")

    username = input("Username: ")
    password = input("Password: ")

    for user in users:

        if (
            user["username"] == username
            and user["password"] == password
            and user["role"] == role
        ):

            print("Login successful!")
            return user

    print("Invalid login details!")
    return None