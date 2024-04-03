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
        


"""
run the application
"""
if __name__ == "__main__":

    show_menu("Python Budgeter")