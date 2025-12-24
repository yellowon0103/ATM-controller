# ATM-controller

This project implements a  **ATM Controller** in Python.

* **Insert Card**: Stores the card number for the current session.
* **PIN Verification**: Authenticates the user via the Bank API.
* **Select Account**: Allows the user to choose from multiple accounts linked to the card, including security checks for account ownership.
* **Transactions**: Supports **Balance Check**, **Deposit**, and **Withdrawal**.
* **Currency**: Handles only 1-dollar bills (integer-based transactions, no cents).

## 📂 Folder Structure & File Descriptions

```text
ATM-controller/
├── main.py                    # Entry point for the interactive simulation.
├── src/
│   ├── controller/
│   │   └── atm_controller.py  # Core state management and transaction logic.
│   ├── services/
│   │   └── bank_service.py    # Abstract interface for bank system integration.
│   └── exceptions.py          # Custom error types for the ATM system.
├── example/
    ├── bank_api_example.py    # MockBankService implementation for testing.
    └── bank_data_example.py   # Sample database with cards, PINs, and balances.
```

## 🚀 How to Run

You can easily run this project on your local machine. Just follow these simple steps:

### 1. Prepare your Environment
First, make sure you have **Conda** installed. Activate your environment like this:
```bash
# Create a new conda environment named 'ATM_conda' with Python 3.9
conda create -n ATM_conda python=3.8

# Activate the environment
conda activate ATM_conda
```
### 2. Run the ATM Simulation
You can start the interactive ATM console by running the main.py file:
```bash
# Start the simulation script
python main.py
```

### 3. Simulation Example & Test Data
For testing, you can refer to the sample data in example/bank_data_example.py. Below is an example of a successful transaction flow:
```bash
> ATM Simulation Start
Insert Card (ex : CARD-001): CARD-001
Card CARD-001 has been recognized.
PIN number: 1234
Correct!
Available accounts: ['001', '002']
Select Account: 001

1. See Balance | 2. Deposit | 3. Withdraw | 4. Exit
Enter the number of your choice: 1
Your current balance is $5000.

1. See Balance | 2. Deposit | 3. Withdraw | 4. Exit
Enter the number of your choice: 2
Enter amount to deposit ($): 10
$10 deposited successfully. Current balance: $5010

1. See Balance | 2. Deposit | 3. Withdraw | 4. Exit
Enter the number of your choice: 1
Your current balance is $5010.

1. See Balance | 2. Deposit | 3. Withdraw | 4. Exit
Enter the number of your choice: 3
Enter amount to withdraw ($): 33
$33 withdrawn successfully. Current balance: $4977

1. See Balance | 2. Deposit | 3. Withdraw | 4. Exit
Enter the number of your choice: 1
Your current balance is $4977.

1. See Balance | 2. Deposit | 3. Withdraw | 4. Exit
Enter the number of your choice: 4
Ejecting card. Thank you for using the ATM.
```