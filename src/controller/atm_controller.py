from typing import List, Optional
from src.services.bank_service import BankService
from src.exceptions import AuthenticationError, NoCardError, UnauthorizedAccountError, InsufficientFundsError

class ATMController:
    def __init__(self, bank_api: BankService):
        self._bank_api = bank_api
        self._current_card_number: Optional[str] = None
        self._is_authenticated: bool = False
        self._selected_account_id: Optional[str] = None

    def insert_card(self, card_number: str) -> None:
        self._current_card_number = card_number
        self._is_authenticated = False
        self._selected_account_id = None

    def validate_pin(self, pin: str) -> bool:
        if not self._current_card_number:
            raise NoCardError("No Card inserted.")

        is_valid = self._bank_api.verify_pin(self._current_card_number, pin)
        self._is_authenticated = is_valid
        return is_valid

    def get_available_accounts(self) -> List[str]:
        if not self._is_authenticated:
            raise AuthenticationError("Need PIN Verification")
        return self._bank_api.get_accounts(self._current_card_number)

    def select_account(self, account_id: str) -> None:
        if not self._is_authenticated:
            raise AuthenticationError("Need PIN Verification")

        owned_accounts = self._bank_api.get_accounts(self._current_card_number)

        if account_id not in owned_accounts:
            raise UnauthorizedAccountError(f"Account {account_id} is not associated with this card.")
        self._selected_account_id = account_id

    def get_account_balance(self) -> int:
        if not self._selected_account_id:
            raise ValueError("No account selected.")
        return self._bank_api.get_balance(self._selected_account_id)

    def deposit_cash(self, amount: int) -> bool:
        if amount <= 0:
            return False

        return self._bank_api.update_balance(self._selected_account_id, amount)

    def withdraw_cash(self, amount: int) -> bool:
        if amount <= 0:
            return False

        current_balance = self.get_account_balance()
        if current_balance < amount:
            raise InsufficientFundsError("Insufficient.")

        success = self._bank_api.update_balance(self._selected_account_id, -amount)
        return success