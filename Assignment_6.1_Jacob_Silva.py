# Made by Jacob Silva for class CIS 245, instructor Allen Voelcker
# This program holds and displays requested static stock prices

# The dictionary holding the values and key names
dictionary = {
    "WMT":      "WMT "      "185",
    "GOOG":     "GOOG "     "170",
    "TGT":      "TGT "      "85",
    "SSUN":     "SSUN "     "95",
    "CNK":      "CNK "      "135",
    "MCD":      "MCD "      "140",
    "TSLA":     "TSLA "     "200",
    "AAPL":     "AAPL "     "215",
    "AMZN":     "AMZN "     "275",
    "MSFT":     "MSFT "     "285"
}


# The main part of the code to prompt an input
def prompt():

    print("Here is a list of the current stocks that you can view: \n"
          "WMT, GOOG, TGT, SSUN, CNK, MCD, TSLA, AAPL, AMZN, MSFT.\n"
          "Please enter them as you see them.\n")
    z = input("Stock name: ")
    x = dictionary.get(z, "That key wasn't recognized, please try again.\n")
    print(x)


prompt()
# The While loop to keep the program running if multiple uses are needed
while True:
    rep = str(input('Please type "y" to restart the program.\n'))

    if rep == "y":
        prompt()
    if rep != "y":
        print("Thank you. Have a nice day!")
        import time
        time.sleep(2)
        break
