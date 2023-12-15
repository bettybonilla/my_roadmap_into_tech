import random
from dataclasses import dataclass
from typing import Optional


@dataclass
class _AccountInformation:
    def __init__(self, name: str, balance: float):
        self.name = name
        self.balance = balance

    def __repr__(self) -> str:
        return f"Name: {self.name}, Balance: ${self.balance:.2f}"


class AccountNumber(int):
    pass


class _Account:
    def __init__(self):
        self.accounts_opened: dict[AccountNumber, _AccountInformation] = {}
        self.available_account_numbers = list(range(10000, 100000))
        random.shuffle(self.available_account_numbers)

    def create_account(self, name: str, initial_deposit: float) -> AccountNumber:
        account_number = self.available_account_numbers.pop(0)
        account_number = AccountNumber(account_number)
        add_account = {account_number: _AccountInformation(name, initial_deposit)}
        self.accounts_opened.update(add_account)
        return account_number

    def display_all_accounts(self):
        print(self.accounts_opened)

    def display_available_balance(self, account_number: AccountNumber):
        account = self.accounts_opened.get(account_number)
        if self.validate_account(account_number):
            print(
                f"\nHello {account.name}, your available balance is ${account.balance:.2f}"
            )

    def deposit(
        self, account_number: AccountNumber, deposit_amount: float
    ) -> Optional[float]:
        account = self.accounts_opened.get(account_number)
        if self.validate_account(account_number):
            account.balance += deposit_amount
            return account.balance
        return None

    def withdraw(
        self, account_number: AccountNumber, withdraw_amount: float
    ) -> Optional[float]:
        account = self.accounts_opened.get(account_number)
        if self.validate_account(account_number):
            if account.balance >= withdraw_amount:
                account.balance -= withdraw_amount
                return account.balance
            return None

    def validate_account(self, account_number: AccountNumber) -> bool:
        account = self.accounts_opened.get(account_number)
        if account:
            return True
        return False


class Bank:
    def __init__(self) -> None:
        self._checking_account = _Account()
        self._savings_account = _Account()

    # Checking
    def create_checking_account(
        self, name: str, initial_deposit: float
    ) -> AccountNumber:
        return self._checking_account.create_account(name, initial_deposit)

    def _display_all_checking_accounts(self):
        self._checking_account.display_all_accounts()

    def display_available_balance_in_checking(self, account_number: AccountNumber):
        self._checking_account.display_available_balance(account_number)

    def deposit_into_checking(
        self, account_number: AccountNumber, deposit_amount: float
    ) -> Optional[float]:
        return self._checking_account.deposit(account_number, deposit_amount)

    def withdraw_from_checking(
        self, account_number: AccountNumber, withdraw_amount: float
    ) -> Optional[float]:
        return self._checking_account.withdraw(account_number, withdraw_amount)

    def validate_checking_account(self, account_number: AccountNumber) -> bool:
        return self._checking_account.validate_account(account_number)

    # Savings
    def create_savings_account(
        self, name: str, initial_deposit: float
    ) -> AccountNumber:
        return self._savings_account.create_account(name, initial_deposit)

    def _display_all_savings_accounts(self):
        self._savings_account.display_all_accounts()

    def display_available_balance_in_savings(self, account_number: AccountNumber):
        self._savings_account.display_available_balance(account_number)

    def deposit_into_savings(
        self, account_number: AccountNumber, deposit_amount: float
    ) -> Optional[float]:
        return self._savings_account.deposit(account_number, deposit_amount)

    def withdraw_from_savings(
        self, account_number: AccountNumber, withdraw_amount: float
    ) -> Optional[float]:
        return self._savings_account.withdraw(account_number, withdraw_amount)

    def validate_savings_account(self, account_number: AccountNumber) -> bool:
        return self._savings_account.validate_account(account_number)


def application_logic():
    chase = Bank()

    print("\nWelcome!")

    while True:
        print("")
        print("--------------------------------------------------------------------")
        print("Enter 1 to create a Checking account")
        print("Enter 2 to create a Savings account")
        print("Enter 3 to access an existing Checking account")
        print("Enter 4 to access an existing Savings account")
        print("Enter 5 to exit")
        print("--------------------------------------------------------------------")
        print("", end="")

        try:
            user_choice_1 = int(input())
        except ValueError:
            print("Please enter a valid choice!")
            continue

        match user_choice_1:
            # Create a Checking account
            case 1:
                print("\nEnter your name:", end=" ")
                name = input()
                print("Enter your initial deposit:", end=" ")
                initial_deposit = float(input())
                user_account_number = chase.create_checking_account(
                    name, initial_deposit
                )
                print("\nCongrats, you have created a Checking account!")
                print(f"Here is your Checking account number: {user_account_number}")
            # Create a Savings account
            case 2:
                print("\nEnter your name:", end=" ")
                name = input()
                print("Enter your initial deposit:", end=" ")
                initial_deposit = float(input())
                user_account_number = chase.create_savings_account(
                    name, initial_deposit
                )
                print("\nCongrats, you have created a Savings account!")
                print(f"Here is your Savings account number: {user_account_number}")
            # Access an existing Checking account
            case 3:
                print("\nEnter your Checking account number:", end=" ")
                account_number = AccountNumber(input())
                if chase.validate_checking_account(account_number):
                    while True:
                        print("")
                        print(
                            "--------------------------------------------------------------------"
                        )
                        print(
                            "Enter 1 to display your available balance in your Checking account"
                        )
                        print("Enter 2 to deposit into your Checking account")
                        print("Enter 3 to withdraw from your Checking account")
                        print("Enter 4 to go back to the previous options")
                        print("Enter 5 to exit")
                        print(
                            "--------------------------------------------------------------------"
                        )
                        print("", end="")

                        try:
                            user_choice_2 = int(input())
                        except ValueError:
                            print("Please enter a valid choice!")
                            continue

                        match user_choice_2:
                            # Display your available balance in your Checking account
                            case 1:
                                chase.display_available_balance_in_checking(
                                    account_number
                                )
                            # Deposit into your Checking account
                            case 2:
                                print("\nEnter the amount to deposit:", end=" ")
                                deposit_amount = float(input())
                                new_balance = chase.deposit_into_checking(
                                    account_number, deposit_amount
                                )
                                print(
                                    f"Your new available balance is ${new_balance:.2f}"
                                )
                            # Withdraw from your Checking account
                            case 3:
                                print("\nEnter the amount to withdraw:", end=" ")
                                withdraw_amount = float(input())
                                new_balance = chase.withdraw_from_checking(
                                    account_number, withdraw_amount
                                )
                                if new_balance is not None:
                                    print(
                                        f"Your new available balance is ${new_balance:.2f}"
                                    )
                                else:
                                    print(
                                        "\nSorry, insufficient balance for withdrawal!"
                                    )
                            # Go back to the previous options
                            case 4:
                                break
                            # Exit
                            case 5:
                                exit(0)
                            case _:
                                print("\nPlease enter a valid choice!")
                else:
                    print("\nSorry, Checking account not found!\n")
                    print(
                        "Please create a Checking account \nor re-enter your Checking account number"
                    )
            # Access an existing Savings account
            case 4:
                print("\nEnter your Savings account number:", end=" ")
                account_number = AccountNumber(input())
                if chase.validate_savings_account(account_number):
                    while True:
                        print("")
                        print(
                            "--------------------------------------------------------------------"
                        )
                        print(
                            "Enter 1 to display your available balance in your Savings account"
                        )
                        print("Enter 2 to deposit into your Savings account")
                        print("Enter 3 to withdraw from your Savings account")
                        print("Enter 4 to go back to the previous options")
                        print("Enter 5 to exit")
                        print(
                            "--------------------------------------------------------------------"
                        )
                        print("", end="")

                        try:
                            user_choice_2 = int(input())
                        except ValueError:
                            print("Please enter a valid choice!")
                            continue

                        match user_choice_2:
                            # Display your available balance in your Savings account
                            case 1:
                                chase.display_available_balance_in_savings(
                                    account_number
                                )
                            # Deposit into your Savings account
                            case 2:
                                print("\nEnter the amount to deposit:", end=" ")
                                deposit_amount = float(input())
                                new_balance = chase.deposit_into_savings(
                                    account_number, deposit_amount
                                )
                                print(
                                    f"Your new available balance is ${new_balance:.2f}"
                                )
                            # Withdraw from your Savings account
                            case 3:
                                print("\nEnter the amount to withdraw:", end=" ")
                                withdraw_amount = float(input())
                                new_balance = chase.withdraw_from_savings(
                                    account_number, withdraw_amount
                                )
                                if new_balance is not None:
                                    print(
                                        f"Your new available balance is ${new_balance:.2f}"
                                    )
                                else:
                                    print(
                                        "\nSorry, insufficient balance for withdrawal!"
                                    )
                            # Go back to the previous options
                            case 4:
                                break
                            # Exit
                            case 5:
                                exit(0)
                            case _:
                                print("\nPlease enter a valid choice!")
                else:
                    print("\nSorry, Savings account not found!\n")
                    print(
                        "Please create a Savings account \nor re-enter your Savings account number"
                    )
            # Exit
            case 5:
                exit(0)
            case _:
                print("\nPlease enter a valid choice!")


if __name__ == "__main__":
    application_logic()
