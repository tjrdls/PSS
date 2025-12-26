from FeePolicy import FeePolicy
from TransactionHistory import TransactionHistory


class Account:
    """
    Represents a bank account.
    """

    def __init__(self, account_id: str, balance: int):
        self.account_id = account_id
        self.balance = balance
        self.fee_policy = FeePolicy()
        self.history = TransactionHistory()

    def deposit(self, amount: int) -> bool:
        if amount <= 0:
            return False

        self.balance += amount
        self.history.record_deposit(self.account_id, amount)
        return True

    def withdraw(self, amount: int) -> bool:
        if amount <= 0:
            return False

        fee = self.fee_policy.calculate_fee(amount)
        total = amount + fee

        if self.balance < total:
            return False

        self.balance -= total
        success = self.history.record_withdraw(self.account_id, amount)
        return success
