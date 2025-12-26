from Account import Account


class BankService:
    """
    Facade for external users.
    """

    def __init__(self):
        self.accounts = {}

    def create_account(self, account_id: str, initial_balance: int) -> None:
        self.accounts[account_id] = Account(account_id, initial_balance)

    def deposit(self, account_id: str, amount: int) -> bool:
        account = self.accounts.get(account_id)
        if not account:
            return False
        return account.deposit(amount)

    def withdraw(self, account_id: str, amount: int) -> bool:
        account = self.accounts.get(account_id)
        if not account:
            return False
        return account.withdraw(amount)
