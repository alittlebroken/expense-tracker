"""Account class

Keyword arguments:
name    - Name for the account
balance - The balance for the account
transactions - Transactions recorded against this account

Return: Nothing
"""
class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transactions = []