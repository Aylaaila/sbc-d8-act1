def read_users():
    try:
        with open("users.txt", "r") as file:
            return dict(line.strip().split(",") for line in file)
    except FileNotFoundError:
        return {}

def write_users(users):
    with open("users.txt", "w") as file:
        file.writelines(f"{u},{p}\n" for u, p in users.items())

def register():
    users = read_users()
    username = input("Username: ")
    if username in users:
        print("Username already exists.")
        return
    password = input("Password: ")
    users[username] = password
    write_users(users)
    print("Registration successful!")

def login():
    users = read_users()
    username = input("Username: ")
    if username not in users:
        print("Username not found.")
        return
    password = input("Password: ")
    if users[username] == password:
        print("Login successful!")
    else:
        print("Incorrect password.")

def change_password():
    users = read_users()
    username = input("Username: ")
    if username not in users:
        print("Username not found.")
        return
    old_password = input("Old password: ")
    if users[username] == old_password:
        new_password = input("New password: ")
        users[username] = new_password
        write_users(users)
        print("Password changed successfully!")
    else:
        print("Incorrect old password.")

def main():
    while True:
        print("\nOptions: 1 - Register, 2 - Login, 3 - Change Password, 4 - Exit")
        choice = input("Choose an option: ").strip().lower()
        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            change_password()
        elif choice == '4':
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()

