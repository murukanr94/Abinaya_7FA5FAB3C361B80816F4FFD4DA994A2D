class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        return f"Account Holder: {self.__account_holder_name}\nAccount Number: {self.__account_number}\nAccount Balance: ${self.__account_balance:.2f}"


# Example usage:
if __name__ == "__main__":
    # Create an instance of BankAccount
    account = BankAccount("123456789", "John Doe", 1000.0)

    # Deposit money
    account.deposit(500.0)

    # Withdraw money
    account.withdraw(200.0)

    # Display account balance
    print(account.display_balance())