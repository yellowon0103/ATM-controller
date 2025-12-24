from src.controller.atm_controller import ATMController
from example.bank_api_example import MockBankService
from src.exceptions import ATMError

def run_atm_simulation():
    # 1. Initialize system (connect to mock bank service)
    bank_api = MockBankService()
    atm = ATMController(bank_api)

    print("> ATM Simulation Start")

    try:
        # 2. Insert Card
        card_number = input("Insert Card (ex : CARD-001): ")
        atm.insert_card(card_number)
        print(f"Card {card_number} has been recognized.")

        # 3. PIN number
        pin = input("PIN number: ")
        if atm.validate_pin(pin):
            print("Correct!")
        else:
            print("Wrong! Exiting program.")
            return

        # 4. Select Account
        accounts = atm.get_available_accounts()
        print(f"Available accounts: {accounts}")
        selected_acc = input("Select Account: ")
        atm.select_account(selected_acc)

        # 5. See Balance/Deposit/Withdraw
        while True:
            print("1. See Balance | 2. Deposit | 3. Withdraw | 4. Exit")
            choice = input("Enter the number of your choice: ")

            if choice == "1":
                balance = atm.get_account_balance()
                print(f"Your current balance is ${balance}.")

            elif choice == "2":
                amount = int(input("Enter amount to deposit ($): "))
                if atm.deposit_cash(amount):
                    print(
                        f"${amount} deposited successfully. "
                        f"Current balance: ${atm.get_account_balance()}"
                    )
                else:
                    print("Deposit failed.")

            elif choice == "3":
                amount = int(input("Enter amount to withdraw ($): "))
                if atm.withdraw_cash(amount):
                    print(
                        f"${amount} withdrawn successfully. "
                        f"Current balance: ${atm.get_account_balance()}"
                    )
                else:
                    print("Withdrawal failed.")

            elif choice == "4":
                print("Ejecting card. Thank you for using the ATM.")
                break
            else:
                print("Invalid selection.")

    except ATMError as e:
        print(f"ATM error occurred: {e}")
    except ValueError:
        print("Please enter numeric values only.")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")


if __name__ == "__main__":
    run_atm_simulation()