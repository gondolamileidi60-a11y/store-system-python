from system import StoreSystem

system = StoreSystem()

while True:
    print("\n--- MAIN MENU ---")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        name = input("Name: ")
        last_name = input("Last name: ")
        email = input("Email: ")
        password = input("Password: ")

        if system.user_manager.register_user(name, last_name, email, password):
            print("User registered successfully.")
        else:
            print("Email already exists.")

    elif choice == "2":
        email = input("Email: ")
        password = input("Password: ")

        user = system.user_manager.login(email, password)
        if user:
            system.current_user = user
            print(f"Welcome {user.name}")
            system.store_menu()
        else:
            print("Invalid credentials.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
