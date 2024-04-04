from src.Account import Account

# List for customer accounts
accounts = []

# The current active account being worked on
selected_account = None

# Create an list of the users current expenses
expenses = []

"""show_menu
Displays the applications main menu

Keyword arguments: None
Return: None
"""
def show_menu():

    global accounts, selected_account

    # Controls the while loop so we can end the program
    # if need be
    running = True
    
    # Run the program until the user decides to quit
    while running:

        print("\n")
        print("Selected account: {}".format(get_account_name(selected_account)))
        print("\n")

        print("Choose an option from below:\n")
        
        print("Accounts [{}]:".format(len(accounts)))
        print("1. List")
        print("2. Select")
        print("3. New")
        print("4. Remove")
        print("\n")

        print("Transactions:")
        print("5. List")
        print("6. Add")
        print("7. Remove")
        print("\n")
        
        print("8. Quit application")
        print("\n")

        option = int(input("> "))

        match option:
            case 1:
                list_accounts()
            case 2:
                select_account()
            case 3:
                new_account()
            case 4:
                remove_account()
            case 5:
                if selected_account != None:
                    accounts[selected_account].show_all_transactions()
            case 6:
                if selected_account != None:
                    accounts[selected_account].add_transaction()
            case 7:
                if selected_account != None:
                    accounts[selected_account].remove_transaction()
            case 8:
                running = False
            case _:
                print("Sorry. That option is not recognised. Please try again.")
        
"""list_accounts

List al accounts for the user running the program

Keyword arguments:
None
Return: Nothing
"""
def list_accounts():
    
    title = "Your account list"
    print("-" * len(title))
    print(title)
    print("-" * len(title))
    print("\n")

    if len(accounts) > 0:
        for idx, account in enumerate(accounts):
            print("{}. {} - £{}".format(idx, account.name, account.balance))
    else:
        print("Currently you have no accounts")
        print("\n")

"""select_account

Allows the user to select an account to perform actions on

Keyword arguments:
None
Return: None
"""
def select_account():
    list_accounts()
    print("\n")
    global selected_account
    if(len(accounts) > 0):

        choice = None
        while choice == None or isinstance(choice, int) == False:
            try:
                choice = int(input("Please enter in the account number: "))
            except Exception:
                choice = None
    
        selected_account = int(choice)


"""new_account

Creates a new account

Keyword arguments:
None
Return: None
"""
def new_account():
    
    global accounts, selected_account

    name = None
    while name == None:
        try:
            name = str(input("Enter new account name: "))
        except Exception:
            name = None
    
    balance = None
    while balance == None:
        try:
            balance = float(input("Please enter in the opening balance: "))
        except Exception:
            balance = None

    accounts.append(Account(name, balance))
    # Get the id of the last added account
    account_id = len(accounts) - 1
    selected_account = int(account_id)
    
    print("Account added")


"""remove_account

Removes the selected account

Keyword arguments:
None
Return: None
"""
def remove_account():
    
    global selected_account
    global accounts

    if len(accounts) < 1:
        return

    list_accounts()    

    print("\n")

    choice = None
    while choice == None or isinstance(choice, int) == False:
        try:
            choice = int(input("Please enter the number of the account you wish to remove: "))
        except Exception:
            choice = None

    del accounts[choice]

    selected_account = None
    print("Account removed")

"""get_account_name

Based on an index number get the account name that matches

Keyword arguments:
id -- The id of the account to display
Return: None
"""
def get_account_name(id):

    global accounts, selected_account

    if len(accounts) < 1:
        return None
    
    if isinstance(id, int) != True:
        return None
    
    return "{} [£{}]".format(accounts[id].name, accounts[id].balance)
    

"""
run the application
"""
if __name__ == "__main__":

    app_title = "Expense Tracker"
    print("\n")
    print("-" * len(app_title))
    print(app_title)
    print("-" * len(app_title))

    show_menu()