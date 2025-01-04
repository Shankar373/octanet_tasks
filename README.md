
# ATM Machine Simulation
This Python program simulates the basic functionalities of an ATM machine, allowing users to perform common banking operations interactively.

## Table of Contents
## Features
## How It Works
## Program Flow
## Requirements
## Usage
## Example Output
## Code
## Notes
##(Features)
1. Balance Inquiry
Check your current account balance instantly.
2. Cash Withdrawal
Withdraw a specified amount if sufficient funds are available.
3. Cash Deposit
Deposit cash into your account and update your balance.
4. Exit
Exit the ATM simulation after completing your transactions.
How It Works
Card Processing
Simulates card insertion with a small delay using the time module.
PIN Authentication
Users must input a 4-digit PIN to access their account.
If the PIN is incorrect, the program terminates with a message.
Interactive Menu
Once authenticated, users can choose from a menu of options.
Each option performs a specific operation and provides feedback.
Error Handling
Input validation ensures numeric entries for PIN, withdrawal, and deposit amounts.
Displays meaningful error messages for invalid inputs or insufficient funds.
Program Flow
Prompt the user to insert a card (simulated).
Request the ATM PIN and authenticate.
Display a menu with options:
1: View Balance
2: Withdraw Cash
3: Deposit Cash
4: Exit
Perform the selected operation and provide feedback.
Repeat until the user chooses to exit.
Requirements
Python 3.x
No additional libraries are required.
Usage
Run the program in a Python environment.
Insert the card (simulated with a delay).
Enter your ATM PIN to authenticate.
Choose an option from the menu and follow the prompts.
Exit the program after completing your transactions.
Example Output
plaintext
Copy code
Please insert your CARD  
Enter your ATM PIN: 1234  

    Please choose from the following options:  
    1. Balance Inquiry  
    2. Cash Withdrawal  
    3. Cash Deposit  
    4. Exit  

Please enter your choice: 1  
Your current balance is: ₹5000  

Please enter your choice: 2  
Enter the amount to withdraw: 1000  
₹1000 has been successfully debited from your account.  
Your updated balance is: ₹4000  

Please enter your choice: 4  
Thank you for using our ATM service. Have a great day!  
Code
python
Copy code
'''
ATM Machine Simulation:

This program simulates basic ATM machine functions, including:
1. Account balance inquiry
2. Cash withdrawal
3. Cash deposit
4. Exit
'''

# Importing time module to simulate card processing delay
import time

print("Please insert your CARD")
time.sleep(5)  

password = 1234  # Default PIN
balance = 5000   # Default balance

try:
    pin = int(input("Enter your ATM PIN: "))  # User input for PIN
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
Notes
This program is a simulation and does not connect to any real banking systems.
Ensure inputs are numeric to avoid errors during transactions.
The default balance is set to ₹5000, and the default PIN is 1234.
Feel free to enhance the program with additional features like transaction history or multi-user support!
