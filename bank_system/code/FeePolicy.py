class FeePolicy:
    """
    Determines fees applied to withdrawals.
    """

    def calculate_fee(self, amount: int) -> int:
        if amount <= 100:
            return 0
        return int(amount * 0.02)
