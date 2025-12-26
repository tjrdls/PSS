class TransactionHistory:
    """
    Stores records of all transactions.
    """

    def __init__(self):
        self.records = []

    def record_deposit(self, account_id: str, amount: int) -> bool:
        self.records.append({
            "account_id": account_id,
            "type": "deposit",
            "amount": amount
        })
        return True

    def record_withdraw(self, account_id: str, amount: int) -> bool:
        if amount <= 0:
            return False

        self.records.append({
            "account_id": account_id,
            "type": "withdraw",
            "amount": amount
        })
        return True
