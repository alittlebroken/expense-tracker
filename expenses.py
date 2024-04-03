from src.Account import Account

# List for customer accounts
accounts = []

# Create an list of the users current expenses
expenses = []

"""show_menu
Displays the applications main menu

Keyword arguments: None
Return: None
"""
def show_menu(app_title):

    # Controls the while loop so we can end the program
    # if need be
    running = True
    
    # Run the program until the user decides to quit
    while running:

        print("\n")
        print("-" * len(app_title))
        print(app_title)
        print("-" * len(app_title))

        print("Choose an option from below:\n")
        
        print("Accounts:")
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
                pass
            case 2:
                pass
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
        

"""list_expenses
List a users current expenses

Keyword arguments: None
Return: None
"""
def list_expenses():
    print("\n")
    print("Current expense list")
    print("--------------------")
    # Check to see if we actually have any expenses to show
    if len(expenses) <= 0:
        print("Currently you have no expenses")
    else:
        # Counter for the loop
        count = 0
        for expense in expenses:
            print("# {} - £{} - {}".format(count, expense["amount"], expense["category"]))
            count += 1


"""addExpense
Add an expense dictionary to the expenses list

Keyword arguments: None
Return: None
"""
def add_expense():

    amount = 0.0
    category = ""

    print("\n")

    print("Please enter in the amount of the expense: ")
    try:
       while True:
           amount = float(input("> "))
           break 
    except:
        print("Error: Invalid entry for expense amount")

    print("Please enter the category for the expense: ")
    try:
        while True:
            category = str(input("> "))
            break
    except:
        print("Error: Invalid entry for expense category")

    # Finally add the expense
    expenses.append({ "amount": amount, "category": category })

    # List the updated expense list
    list_expenses()

"""remove_expense
Removes the selected expense

Keyword arguments: None
Return: None
"""
def remove_expense():
    list_expenses()
    
    # If no expenses skip the rest of the function
    if len(expenses) < 1:
        return
    
    print("Please enter the number of the expense to remove: ")
    try:
        while True:
            id = int(input("> "))
            break
    except:
        print("Error: Invalid entry for expense id")
    
    # Remove the expense
    expenses.pop(id)
    list_expenses()

"""
run the application
"""
if __name__ == "__main__":

    show_menu("Python Budgeter")