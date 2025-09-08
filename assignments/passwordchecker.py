"""
The program checks if a password is strong based on criteria: minimum length of 8 characters, 
at least one uppercase letter, one lowercase letter, and one digit.
It uses a loop to repeatedly ask for a password until a strong one is entered.
The code uses conditional statements (if, elif, else) to validate the password against the criteria.
The code is wrapped in a function (password_checker) for neatness and reusability.

"""




# Defines a function called password_checker.
def password_checker():
    while True:
        password = input("Enter a password: ") # Keeps asking for a password until a strong one is entered. input() collects user input.

        # These flags track whether the password has: one uppercase letter, one lowercase letter, and one digit.
        has_upper = False
        has_lower = False
        has_digit = False

        # Goes through each character in the password. Sets flags to True if conditions are met.
        for char in password:
            if char.isupper():
                has_upper = True
            elif char.islower():
                has_lower = True
            elif char.isdigit():
                has_digit = True

        # First checks if the password has minimum length of 8.
        # Then checks for uppercase, lowercase, and digit.
        # If all conditions are satisfied → prints success message and breaks out of the loop.
        if len(password) < 8:
            print("Password too short! Must be at least 8 characters.")
        elif not has_upper:
            print("Password must contain at least one uppercase letter.")
        elif not has_lower:
            print("Password must contain at least one lowercase letter.")
        elif not has_digit:
            print("Password must contain at least one number.")
        else:
            print("Strong password set successfully!")
            break  # exit loop when valid


# Run the program
password_checker()
