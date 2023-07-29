# Made by Jacob Silva and based on the provided video
# for class CIS 245, instructor Allen Voelcker.
"""Program to convert gallons to liters"""


def main():
    # Introduction
    print("This program calculates the amount of liters in a given \n"
          "amount of gallons. The conversion rate for this program \n"
          "will be 1 gallon = 3.785 liters.")
    print()
    try:
        # Get number of gallons
        gallons_inputted = float(input("Please enter the number of gallons: "))
        calculation(gallons_inputted)
        repeat()
    except:
        print("An error has occurred, please try again with only a number.")
        print()
        main()


# Calculates gallons into liters
def calculation(gallons_inputted):
    liters = gallons_inputted * 3.785
    print()
    print(f"{gallons_inputted} gallons is equal to {liters} liters.")


# Restarts the main function
def repeat():
    response = input("Would you like to go again? Press y to do so. "
                     "Press n to stop.\n")
    if response == 'y':
        main()
    if response == 'n':
        print("Goodbye!")


main()
