class ATMError(Exception):
    pass

class NoCardError(ATMError):
    pass

class AuthenticationError(ATMError):
    pass

class UnauthorizedAccountError(ATMError):
    pass

class InsufficientFundsError(ATMError):
    pass