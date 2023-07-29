while True:
    # Created by Jacob Silva for class CIS 245, instructor Allen Voelcker
    cost = 0.87

    # Gathering inputs.
    company_name = (input("Hello. This is the Fiber Optic Ordering System. Please input your company's title: "))
    feet_of_wire = (input("Thank you. Please enter the number of feet of Fiber Optic wire you would like to buy? "))
    # Um...
    if float(feet_of_wire) <= 0:
        print("I'm sorry, an error has occurred. Please try again.")
        continue
    total = cost*float(feet_of_wire)
    print(f"Great! Here is your total for {company_name.title()}: ")
    print(str(total))

    # The loop around.
    response = (input("Would you like to make another purchase? Please press y to do so. "))
    if response == "y":  # Return to line 6.
        continue
    if response != "y":  # End the program.
        print("Goodbye!")
        break
