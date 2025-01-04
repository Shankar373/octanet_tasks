'''
ATM Machine Simulation:

This program simulates basic ATM machine functions, including:
1. Account balance inquiry
2. Cash withdrawal
3. Cash deposit
4. Exit
'''

# Importing time module to simulate c
import time
print("Please insert your CARD")
time.sleep(5)  

password = 1234
balance = 5000  
try:
    pin = int(input("Enter your ATM PIN: "))
except ValueError:
    print("Invalid input! Please enter a numeric PIN.")
    exit()

if pin == password:
    while True:
        print("""
        Please choose from the following options:
        1. Balance Inquiry
        2. Cash Withdrawal
        3. Cash Deposit
        4. Exit
        """)

        try:
            # Taking user choice
            option = int(input("Please enter your choice: "))
        except ValueError:
            print("Invalid choice! Please select a valid option.")
            continue

        # Option 1: Balance Inquiry
        if option == 1:
            print(f"Your current balance is: ₹{balance}")

        # Option 2: Cash Withdrawal
        elif option == 2:
            try:
                withdraw_amount = int(input("Enter the amount to withdraw: "))
                if withdraw_amount > 0:
                    if balance >= withdraw_amount:
                        balance -= withdraw_amount
                        print(f"₹{withdraw_amount} has been successfully debited from your account.")
                        print(f"Your updated balance is: ₹{balance}")
                    else:
                        print(f"Insufficient funds! Your current balance is ₹{balance}.")
                else:
                    print("Invalid amount! Please enter a positive number.")
            except ValueError:
                print("Invalid input! Please enter a valid numeric value.")

        # Option 3: Cash Deposit
        elif option == 3:
            try:
                deposit_amount = int(input("Enter the amount to deposit: "))
                if deposit_amount > 0:
                    balance += deposit_amount
                    print(f"₹{deposit_amount} has been successfully credited to your account.")
                    print(f"Your updated balance is: ₹{balance}")
                else:
                    print("Invalid amount! Please enter a positive number.")
            except ValueError:
                print("Invalid input! Please enter a valid numeric value.")

        # Option 4: Exit
        elif option == 4:
            print("Thank you for using our ATM service. Have a great day!")
            break

        else:
            print("Invalid choice! Please select a valid option.")
else:
    print("Wrong PIN! Please try again.")
