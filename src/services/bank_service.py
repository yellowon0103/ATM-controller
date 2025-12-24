from abc import ABC, abstractmethod
from typing import List

class BankService(ABC):
    @abstractmethod
    def verify_pin(self, card_number: str, pin: str) -> bool:
        # Check PIN Number
        pass

    @abstractmethod
    def get_accounts(self, card_number: str) -> List[str]:
        # Return Available Accounts
        pass

    @abstractmethod
    def get_balance(self, account_id: str) -> int:
        # See Balance
        pass

    @abstractmethod
    def update_balance(self, account_id: str, amount: int) -> bool:
        # Update Balance
        pass