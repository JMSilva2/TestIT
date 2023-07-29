# Made by Jacob Silva for class CIS 245, instructor Allen Voelcker
# This program converts miles to kilometers
def main():
    # This function begins all the other functions
    intro()
    conversion()
    repeat()


def intro():
    # Intro of the program using a function
    print("\nHello, this program is made to convert a given amount of miles\n"
          "into kilometers. The formula for this program is 1 mile to 1.609\n"
          "kilometers. Please type your answer out as a positive real number.\n")


def conversion():
    # Collecting and utilizing the data given by the user
    try:
        miles = float(input('Please type in the amount of miles as a number. Eg. "30".\n'))
        if miles <= 0:
            print("I'm sorry, but this program asks that you\n"
                  "please input positive numbers only.\n")
            conversion()
        kilometer = miles * 1.609
        print(f"{miles} miles is equal to {kilometer} kilometers.")
    except:
        print("I'm sorry, I couldn't read that value.\n"
              "Please make sure it is a numerical value and try again\n")
        conversion()


def repeat():
    # Function to restart the program if desired so
    rep = str(input('Please type "y" to restart the program.\n'))

    if rep == "y":
        main()
    if rep != "y":
        print("Thank you. Have a nice day!")
        import time
        time.sleep(2)


main()
