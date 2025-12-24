import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from src.services.bank_service import BankService
from example.bank_data_example import BANK_DATA

class MockBankService(BankService):
    def __init__(self):
        self.bank_database = BANK_DATA

    def verify_pin(self, card_number: str, pin: str) -> bool:
        if card_number in self.bank_database:
            return self.bank_database[card_number]["pin"] == pin
        return False

    def get_accounts(self, card_number: str) -> list:
        if card_number in self.bank_database:
            return list(self.bank_database[card_number]["accounts"].keys())
        return []

    def get_balance(self, account_id: str) -> int:
        for card_info in self.bank_database.values():
            if account_id in card_info["accounts"]:
                return card_info["accounts"][account_id]
        return 0

    def update_balance(self, account_id: str, amount: int) -> bool:
        for card_info in self.bank_database.values():
            if account_id in card_info["accounts"]:
                card_info["accounts"][account_id] += amount
                return True
        return False
