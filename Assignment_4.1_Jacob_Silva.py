# Created by Jacob Silva for class CIS 245, instructor Allen Voelcker
while True:
    # Declare the year
    year = 0
    # Gather the interest rate
    interest_rate = float(input("Please input your interest rate as a whole number.\n"
                                "For example, 10 will be 10%. "))
    # Turn the interest rate into a decimal
    original_rate = interest_rate
    interest_rate = interest_rate/100
    actual_rate = 1.00 + interest_rate
    # Gather the initial investment
    initial_investment = float(input('Please enter initial investment as a whole number.\n'
                                     'For example, 15000 will be $15,000. '))
    # Declare the target and original amount
    original_amount = float(initial_investment)
    expected_amount = float(initial_investment)*2
    print(f'Here is a list on how much will be added\n'
          f'to your investment on your way to {expected_amount}')
    # While loop for determining total investment after each year
    while float(initial_investment) < expected_amount:
        print(f'Year: {year}. Investment amount: {initial_investment}')
        initial_investment = initial_investment * actual_rate
        year += 1
        if float(initial_investment) > expected_amount:
            print(f'It will take you {year} years to get {initial_investment}')
            print(f'from an initial investment of ${original_amount}\n'
                  f'at a rate of {original_rate}% per year.')
            break
    print('')
    response = input('Would you like to go again?\n'
                     'Please press "y" to go again. ')
    if response == 'y':
        print('')
        continue
    else:
        break
