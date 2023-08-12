# Made by Jacob Silva for class CIS 245, instructor Allen Voelcker
# This program is designed to take in info and both display it
# Back to the user and create a .txt file using the given information

# Primary functionality of program
def file_amend():
    # Gathering info
    file = input("Please input the file name: \n")
    user = input("Please input your first name: \n")
    st_add = input("Please input your address: \n")
    num = input("Please input your phone number: \n")
    # Displaying collected info
    file_sum = f"{user}, {st_add}, {num}. These values belong to the {file} file."
    print(str(file_sum))
    # Creating a file based on the info
    file_name = f'{file}'
    with open(file_name, 'w') as file_object:
        file_object.write(f'{file_sum}')


# Ability to repeat program if needed
def repeat():
    answer = input("Would you like to edit this information? Press 'y' for yes and 'n' for no.")
    if answer == "y":
        file_amend()
    if answer == "n":
        print("Thank you. Please enjoy your new .txt file!")
        import time
        time.sleep(2)

    else:
        print("Please try again.")
        print("")
        repeat()


# Beginning the program
file_amend()
repeat()
