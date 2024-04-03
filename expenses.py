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

    # Controls the while loop so we can end the program
    # if need be
    running = True
    
    # Run the program until the user decides to quit
    while running:

        print("\n")
        print("Current active account: {}".format(selected_account))
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
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
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
            print("{}. {}".format(idx, account[idx].name))
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

    if(len(accounts) > 0):

        choice = None
        while choice == None or choice.isdigit() != False:
            try:
                choice = int(input("Please enter in the account number: "))
            except Exception:
                choice = None
    
        selected_account = int(choice)



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