from Expense import Expense
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

    """show_filtered_transactions

    Displays transactions that belong to a certain category
    
    Keyword arguments: None
    Return: Nothing
    """
    def show_filtered_transactions(self):
        
        # Display list of categories
        catCount = 0
        for cat in self.categories:
            print("{}. {}".format(catCount, cat["name"]))
            catCount += 1

        choice = ""
        while True:
            try:
                choice = str(input("Please enter in the category name: "))
                break
            except:
                print("Invalid category name")

        
        print("Transactions filtered by {}".format(choice))
        for trans in self.transactions:
            if trans["category"] == choice:
                print("{} - £{}".format(trans["name"], trans["amount"]))


    """add_transaction

    Adds a new transaction to this account
    
    Keyword arguments: None
    Return: Nothing
    """
    def add_transaction(self):
        print("Add new transaction for account: {}".format(self.name))

        name = None
        while name == None:
            try:
                name = str(input("Name of the transaction: "))
            except Exception:
                name = None
        
        amount = None
        while amount == None or amount.isfloat() == False:
            try:
                amount = float(input("Amount of the transaction: "))
            except Exception:
                amount = None

        category = None
        while category == None:
            try:
                category = str(input("Category of the transaction: "))
            except Exception:
                category = None

        trans_type = None
        while trans_type == None or (trans_type != "CREDIT" or trans_type != "DEBIT"):
            try:
                trans_type = str(input("Type of transaction [CREDIT/DEBIT]: "))
            except Exception:
                trans_type = None

        # Finally ad the transaction
        self.transactions.append(Expense(name, amount, category, trans_type))
                
    