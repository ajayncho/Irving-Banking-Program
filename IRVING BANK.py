# Banking Program  #includes page decorations
# I use the def function 
# So i can reuse it whenever i want to show the balance, without repeating print statements every time.

def show_balance(balance):
    print('----------------------------')
    print(f"Your balance is ${balance:.2f}")
    print('----------------------------')

def deposit():
    amountst = input("Enter the amount that you want to be deposited: ")
    if amountst.replace('.', '', 1).isdigit():
        amount = float(amountst)
    else:
        print("Invalid input: Please enter a numeric value.")
        return 0
    print('----------------------------')
    
    if amount < 0:
        print('----------------------------')
        print("Error: That's not a valid amount")
        print('----------------------------')
        return 0
    else:
        return amount
    
def withdraw(balance):
    amountst = input("Enter the amount that you want to be withdrawn: ")
    if amountst.replace('.', '', 1).isdigit():
        amount = float(amountst)
    else:
        print("Invalid input: Please enter a numeric value.")
        return 0
    print('----------------------------')
    if amount > balance:
        print('----------------------------')
        print('Insufficient Funds')
        print('----------------------------')
        return 0
    elif amount < 0:
        print('----------------------------')
        print('Error: Amount must be greater than 0')
        print('----------------------------')
        return 0
    else:
        return amount

# this is a python dictionary filled with bank account ID and names
bank_accounts = { '1001': {'name': 'Charles Abafah', 'password': 'garieru12', 'balance': 250_430.00,},
    '1002': {'name': 'Leo Ntemba', 'password': 'ndoleplantain11', 'balance': 220_346.00},
    '1003': {'name': 'Hilda Kong', 'password': 'ricestew21', 'balance': 145_560.00}
}


def main():
    # Loop until user enters a valid Irving Bank ID
    while True:
        # Ask for Irving Bank ID
        irving_id = input("Welcome to Irving Bank! What is your Irving Bank ID? ")
        print('----------------------------')

        # Getting the user name connected to the ID or show error if ID not found
        if irving_id in bank_accounts:
            name = bank_accounts[irving_id]
            password = input("Please enter your password: ")
            print('----------------------------')

            # Verify password
            if password == bank_accounts[irving_id]['password']:
                name = bank_accounts[irving_id]['name']
                print(f"Welcome, {name}!")
                print('----------------------------')
                user = bank_accounts[irving_id]
                break
            else:
                print("Incorrect password. Try again.")
                print('----------------------------')
        else:
            print("Error: Bank ID not found, try again.")
            print('----------------------------')

    is_running = True
    # While loop: as long as it is running true the while loop will keep looping
    while is_running:
        print('----------------------------')
        print("    Banking Program    ")
        print('----------------------------')
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print('----------------------------')
        
        # Get the user’s choice
        choice = input('Enter your choice (1-4): ')
        
        # Process the choice
        if choice == '1':
            show_balance(user['balance'])
        elif choice == '2':
           user['balance'] += deposit()
        elif choice == '3':
            user['balance'] -= withdraw(bank_accounts[irving_id]['balance'])
        elif choice == '4':
            is_running = False
        else:
            print('----------------------------')
            print("Error: Invalid Choice")
            print('----------------------------')
    
    print('----------------------------------')
    print('Thank you! Have a wonderful day!')
    print('----------------------------------')

# This means if the script is run directly, it starts by calling main(),
# but if it's imported into another file, the banking code won't run automatically.
if __name__ == '__main__':
    main()
