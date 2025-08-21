# Irving-Banking-Program
This Python banking program simulates account management with secure login using bank ID and password. Users can view balances, deposit funds with validation, and withdraw with checks for errors or insufficient balance. It uses functions for modularity, loops for interactivity, and clear messages for a realistic banking experience.
✨ Features

🔑 Secure Login – Users authenticate with a unique bank ID and password.

💰 Check Balance – Display current account balance in a clear format.

➕ Deposit Funds – Input validation ensures deposits are numeric and positive.

➖ Withdraw Funds – Validates inputs and prevents overdrafts or invalid withdrawals.

🔄 Interactive Menu – Loop-driven interface lets users perform multiple actions until exit.

🛠️ Modular Design – Functions (show_balance, deposit, withdraw) keep the program organized and reusable.

📂 Project Structure
IRVING_BANK_BANKING_PROGRAM/
│
├── banking_program.py   # Main Python file with banking logic
├── README.md            # Project documentation
└── LICENSE              # Project license (MIT recommended)

🚀 Getting Started
Prerequisites

Python 3.8+

Installation

Clone this repository:

git clone https://github.com/ajayncho/irving-bank.git
cd irving-bank


Run the program:

python banking_program.py

🖥️ Usage

Start the program and log in using one of the stored Bank IDs and passwords.
Example accounts are preloaded in the dictionary:

Bank ID	Name	Password	Balance
1001	Charles Abafah	garieru12	250,430.00
1002	Leo Ntemba	ndoleplantain11	220,346.00
1003	Hilda Kong	ricestew21	145,560.00

Choose an option from the menu:

----------------------------
    Banking Program    
----------------------------
1. Show Balance  
2. Deposit  
3. Withdraw  
4. Exit  


Perform transactions until you choose to exit.

📖 Example Walkthrough
Welcome to Irving Bank! What is your Irving Bank ID? 1001
Please enter your password: garieru12
----------------------------
Welcome, Charles Abafah!
----------------------------
    Banking Program
----------------------------
1. Show Balance
2. Deposit
3. Withdraw
4. Exit
----------------------------
Enter your choice (1-4): 1
----------------------------
Your balance is $250430.00
----------------------------

📚 Concepts Demonstrated

Functions and modular programming

Dictionaries for data storage

Input validation and error handling

While loops for interactivity

Conditional statements for decision-making

📜 License

This project is licensed under the MIT License – see the LICENSE
 file for details.

🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to improve.
