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
        print("\n-------------------")
        print("Python Expenses App")
        print("-------------------\n")
        print("You can perform the following:\n")
        print("1. Add expense")
        print("2. Remove expense")
        print("3. List expenses")
        print("4. Quit application")
        print("\n")

        option = input("> ")

        if option == "1":
            add_expense()
        elif option == "2":
            remove_expense()
        elif option == "3":
            list_expenses()
        elif option == "4":
            running = False
        else:
            print("Please try again that option is not recognised")
    
    print("\nThank you for using the Python expenses app")
        

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
    show_menu()