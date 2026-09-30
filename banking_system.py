# Banking System Using Python

# Sample account details
account_number = "123456"
pin = "1234"
balance = 10000.0

print("================================")
print("       BANKING SYSTEM")
print("================================")

# Account Login
username = input("Enter account number: ")
password = input("Enter PIN: ")

if username == account_number and password == pin:

    print("\nLogin successful!")
    
    while True:
        print("\n========== MENU ==========")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice: ")

        # Deposit
        if choice == "1":
            amount = float(input("Enter deposit amount: "))

            if amount > 0:
                balance += amount
                print("Deposit successful!")
                print("Current balance:", balance)
            else:
                print("Deposit amount must be greater than zero.")

        # Withdrawal
        elif choice == "2":
            amount = float(input("Enter withdrawal amount: "))

            if amount <= 0:
                print("Withdrawal amount must be greater than zero.")
            elif amount > balance:
                print("Insufficient balance.")
            else:
                balance -= amount
                print("Withdrawal successful!")
                print("Remaining balance:", balance)

        # Check Balance
        elif choice == "3":
            print("Current balance:", balance)

        # Exit
        elif choice == "4":
            print("Thank you for using the Banking System.")
            break

        else:
            print("Invalid choice. Please try again.")

else:
    print("Invalid account number or PIN.")
