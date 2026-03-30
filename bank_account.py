import unittest

class BankAccount:
    def __init__(self, name, balance):
        if balance < 0:
            raise ValueError("Saldo awal tidak boleh negatif")
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance


# ================= UNIT TEST =================
class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount("Putri", 100)

    def test_deposit(self):
        self.assertEqual(self.account.deposit(50), 150)

    def test_withdraw(self):
        self.assertEqual(self.account.withdraw(50), 50)

    def test_get_balance(self):
        self.assertEqual(self.account.get_balance(), 100)

    def test_withdraw_over_balance(self):
        self.assertEqual(self.account.withdraw(200), 100)


# ================= MAIN PROGRAM =================
def main():
    print("=== SIMULASI BANK ACCOUNT ===\n")

    acc = BankAccount("Putri", 100)
    print("Saldo awal:", acc.get_balance())

    acc.deposit(50)
    print("Setelah deposit 50:", acc.get_balance())

    acc.withdraw(30)
    print("Setelah withdraw 30:", acc.get_balance())

    acc.withdraw(200)
    print("Coba withdraw 200 (gagal):", acc.get_balance())

    print("\n=== TESTING ===")


if __name__ == "__main__":
    main()
    print()  # biar rapi
    unittest.main(argv=['first-arg-is-ignored'], exit=False)