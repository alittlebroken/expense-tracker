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

    """show_all_transactions

    Displays the list of transactions this account has
    
    Keyword arguments: None
    Return: Nothing
    """
    def show_all_transactions(self):

        # Counter for ID of transaction
        counter = 0
        print("All transactions for account: {}".format(self.name))
        for transaction in self.transactions:
            print("{}. {} - £{} - {}".format(
                counter,
                transaction.name,
                transaction.amount,
                transaction.category
            ))

    
    