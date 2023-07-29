print("Hello! This is the Fiber Optic Ordering System.")
while True:
    # Created by Jacob Silva for class CIS 245, instructor Allen Voelcker
    cost_0 = 0.87
    cost_1 = 0.80
    cost_2 = 0.70
    cost_3 = 0.50
    # Gathering inputs.
    company_name = (input("Please input your company's title: "))
    print("Thank you!")
    feet_of_wire = (input("Please enter the number of feet of Fiber Optic wire you would like to buy? "))
    # If statements for determining cost
    if 0 < float(feet_of_wire) < 100:
        total = cost_0*float(feet_of_wire)
        print(f"Great! Here is your total for {company_name.title()}: ")
        print(str(total))
    elif 100 <= float(feet_of_wire) < 250:
        total = cost_1 * float(feet_of_wire)
        print(f"Great! Here is your total for {company_name.title()}: ")
        print(str(total))
    elif 250 <= float(feet_of_wire) < 500:
        total = cost_2 * float(feet_of_wire)
        print(f"Great! Here is your total for {company_name.title()}: ")
        print(str(total))
    else:
        total = cost_3 * float(feet_of_wire)
        print(f"Great! Here is your total for {company_name.title()}: ")
        print(str(total))
    # The loop around.
    print("Would you like to make another purchase?")
    response = (input(" Please press y to do so. "))
    if response == "y":  # Return to line 8.
        continue
    if response != "y":  # End the program.
        print("Goodbye!")
        break
