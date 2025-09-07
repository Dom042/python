def atm_simulator():
    balance = 1000  # starting balance
    
    print("💳 Welcome to Simple ATM Simulator")
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    
    try:
        choice = int(input("Choose an option: "))

        if choice == 1:
            print(f"✅ Your current balance is: ${balance}")

        elif choice == 2:
            amount = float(input("Enter deposit amount: $"))
            if amount <= 0:
                print("❌ Deposit amount must be greater than 0.")
            else:
                balance += amount
                print(f"✅ Transaction successful! New balance: ${balance}")

        elif choice == 3:
            amount = float(input("Enter withdrawal amount: $"))
            if amount <= 0:
                print("❌ Withdrawal amount must be greater than 0.")
            elif amount > balance:
                print("❌ Insufficient funds! Transaction cancelled.")
            else:
                balance -= amount
                print(f"✅ Transaction successful! New balance: ${balance}")

        else:
            print("❌ Invalid option! Please select 1, 2, or 3.")

    except ValueError:
        print("❌ Invalid input! Please enter a number.")


# Run the ATM simulator
atm_simulator()
