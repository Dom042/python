def password_checker():
    while True:
        password = input("Enter a password: ")

        # Criteria flags
        has_upper = False
        has_lower = False
        has_digit = False

        # Loop through characters
        for char in password:
            if char.isupper():
                has_upper = True
            elif char.islower():
                has_lower = True
            elif char.isdigit():
                has_digit = True

        # Check conditions
        if len(password) < 8:
            print("❌ Password too short! Must be at least 8 characters.")
        elif not has_upper:
            print("❌ Password must contain at least one uppercase letter.")
        elif not has_lower:
            print("❌ Password must contain at least one lowercase letter.")
        elif not has_digit:
            print("❌ Password must contain at least one number.")
        else:
            print("✅ Strong password set successfully!")
            break  # exit loop when valid


# Run the program
password_checker()
