from src.Expense import Expense
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

    """show_summary

    Shows details of n instance of this Account class

    
    Keyword arguments: None
    Return: None
    """
    def show_summary(self):
        print("\n")
        text = "Summary for {} account".format(self.name)
        print(text)
        print("-" * len(text))
        print("\n")
        print("Balance: £{}".format(self.balance))
        print("Transactions: {}".format(len(self.transactions)))
        
    

    """show_all_transactions

    Displays the list of transactions this account has
    
    Keyword arguments: None
    Return: Nothing
    """
    def show_all_transactions(self):

        # Counter for ID of transaction
        counter = 0
        text = "All transactions for account: {}".format(self.name)
        print("\n")
        print("-" * len(text))
        print(text)
        print("-" * len(text))
        print("\n")
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
        while amount == None or isinstance(amount, float) == False:
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
        while trans_type == None:
            try:
                trans_type = str(input("Type of transaction [CREDIT/DEBIT]: "))
                if trans_type == "DEBIT" or trans_type == "CREDIT":
                    pass
                else:
                    trans_type = None
            except Exception:
                trans_type = None

        # Finally add the transaction
        self.transactions.append(Expense(name, amount, category, trans_type))

        # Show current transactions
        self.show_all_transactions()

    """remove_transaction
    
    Keyword arguments: None
    
    Return: None
    """
    def remove_transaction(self):

        # prompt the user if they wish to see all transaction or select a category?
        choice = None
        while choice == None:
            try:
                print("Type ALL for all transactions or FILTER to apply a filter: ")
                choice = str(input("> "))
            except Exception:
                choice = None

        if(choice == "All"):
            self.show_all_transactions()
        else:
            cat = None
            while cat == None:
                try:
                    cat = str(input("Category to filter by: "))
                except Exception:
                    cat = None

            # Filter the transactions
            print("Showing transactions filtered by: {}".format(cat))
            for idx, trans in enumerate(self.transactions):
                if(trans["category"] == cat):
                    print("{}. {} - £{} - {}".format(idx, trans["name"], trans["amount"], trans["category"]))

        # Prompt the user for the ID of the transaction to be affected
        choice = None
        while choice == None or choice.isdigit() != False:
            try: 
                choice = int(input("Enter the id of the transaction to remove: "))
            except Exception:
                choice = None

        # Now remove the selected transaction
        self.transactions.remove(choice)


    