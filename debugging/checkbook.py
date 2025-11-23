#!/usr/bin/python3
"""
Checkbook Management Program

This program allows a user to manage a simple checkbook with the following features:
- Deposit money
- Withdraw money
- Check current balance
- Exit the program

All inputs are validated to prevent crashes due to invalid entries.
"""

class Checkbook:
    """
    A simple Checkbook class to track balance and perform basic operations.

    Attributes:
        balance (float): The current balance of the checkbook.
    """

    def __init__(self):
        """Initialize the checkbook with a balance of 0.0."""
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit a specified amount into the checkbook.

        Parameters:
            amount (float): The amount of money to deposit. Must be non-negative.

        Behavior:
            Updates the balance and prints the deposited amount and current balance.
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the checkbook.

        Parameters:
            amount (float): The amount of money to withdraw. Must be non-negative.

        Behavior:
            If sufficient funds exist, updates the balance and prints the withdrawn amount and new balance.
            Otherwise, prints a message indicating insufficient funds.
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Print the current balance of the checkbook.
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Main program loop.

    Behavior:
        Prompts the user to choose an action: deposit, withdraw, balance, or exit.
        Handles invalid commands and non-numeric input gracefully.
    """
    cb = Checkbook()

    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()

        if action == 'exit':
            print("Goodbye!")
            break

        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                if amount < 0:
                    print("Amount cannot be negative.")
                else:
                    cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                if amount < 0:
                    print("Amount cannot be negative.")
                else:
                    cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        elif action == 'balance':
            cb.get_balance()

        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()

    
