# Event Registration App

# List to store registered people in order
registrations = []


def register_person():
    """Function for a person to register"""
    name = input("Enter your name: ").strip()
    if name:
        registrations.append(name)
        print(f"✅ {name}, you have been registered successfully! Your number is {len(registrations)}.")
    else:
        print("❌ Name cannot be empty!")


def admin_view():
    """Function for admin to view all registered people"""
    if not registrations:
        print("⚠️ No one has registered yet.")
    else:
        print("\n📋 List of registered people (in order of arrival):")
        for i, person in enumerate(registrations, start=1):
            print(f"{i}. {person}")
    print()


def main():
    while True:
        print("\n=== Event Registration App ===")
        print("1. Register as a person")
        print("2. Admin view registrations")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            register_person()
        elif choice == "2":
            admin_view()
        elif choice == "3":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid option! Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
