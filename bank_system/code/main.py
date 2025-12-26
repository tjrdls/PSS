from bank_system.code import BankService

bank = BankService()
bank.create_account("alice", 1000)

print("Deposit:", bank.deposit("alice", 200))
print("Withdraw:", bank.withdraw("alice", 300))
print("Withdraw too much:", bank.withdraw("alice", 2000))
