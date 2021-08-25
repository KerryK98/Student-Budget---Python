print('\t CPS109 (Assignment 1) Kerry Kanhai - 501063750 \t')
print('\t Hello, This is Your Annual Budget\t')

# Function called Student that asks for Student information
def student(student_name):
    savings = 0
    total_bank = 0
    total_monthly = 0
    total_year = 0

    program = input('What program are you enrolled in? : ')

    # Adds values to the following variables by calling the appropriate methods
    savings = add_savings()
    government_funding = add_funding()
    tuition = add_tuition()

    # Calculates how much the user would having with government funding
    total_bank = float(savings) + float(government_funding)

    print_stars()

    print(f'Total amount currently in your bank account before deductions are: {total_bank}')

    print_stars()

    # Displays student information by calling the display_student function
    display_student(savings, government_funding, tuition)

    print_stars()

    # Calls the appropriate methods to ask for user input for their expenses
    rent = add_rent()
    personal = add_personal()
    groceries = add_groceries()
    insurance = add_insurance()
    entertainment = add_entertainment()

    expenses = [rent, personal, groceries, insurance, entertainment]

    # Calculates annual costs of each of the expenses and adds it to a total cost
    for expense in expenses:
        annual_expense = float(expense) * 12
        total_year += annual_expense

    # Calculates the monthly expenses for each category
    total_monthly = float(total_year) / 12

    print_stars()

    # Displays student's expenses
    student_personalexp(student_name, rent, personal, groceries, insurance, entertainment, total_year, total_monthly)

    if rent <= 0:
        print('You do not have rent expenses')
    if entertainment <= 0:
        print('You do not have entertainment expenses')

    total_deductions = float(total_bank) - float(total_year)
    print(f'Your total after deductions are: $ {total_deductions}')

    if total_deductions <= 0:
        print("You do not have enough money to compensate for your budget")


# Function that processes information for non students
def non_student(nonstudent_name):
    annual_income = 0
    savings = 0
    total_year = 0
    expenses = []
    employed = False
    difference = 0
    total_deductions = 0
    total_monthly = 0
    total_bank = 0

    # If user is working, they are asked to input their annual income
    working = input("Do you have a job (Y/N): ")
    if working.lower() == 'y':
        annual_income = add_income()
        employed = True

    savings = add_savings()

    # Adds all expenses to a list
    expenses.append(add_rent())
    expenses.append(add_utilities())
    expenses.append(add_personal())
    expenses.append(add_insurance())
    expenses.append(add_groceries())

    # Calculates annual costs of each of the expenses and adds it to a total cost
    for expense in expenses:
        annual_expense = expense * 12
        total_year += annual_expense

    # If the person is employed, the difference between total yearly expenses and annual income is taken
    if employed:
        total_bank = savings + annual_income
    else:
        total_bank = savings

    print_stars()

    total_deductions = round(total_bank - total_year, 2)

    total_monthly = float(total_year) / 12

    # Calls the appropriate function print the information
    display_info(nonstudent_name, annual_income, savings, total_year, expenses, total_deductions, total_monthly)

    if total_deductions <= 0:
        print('You do not have enough money to compensate for your budget')


# Function that prints out student information
def display_student(savings, government_funding, tuition):
    print(f'Savings: {savings}')
    print(f'Government Funding: {government_funding}')
    print(f'Students Annual Tuition: {tuition}')

# Asks for government funding input and validates input
def add_funding():
    government_funding = float(input('Please enter total government funding: $'))
    if government_funding <= 0:
        print("You are not eligible for funding")

    return government_funding

# Asks for tuition input and validates input
def add_tuition():
    tuition = float(input('Please enter annual tuition: $ '))
    return tuition

# Displays student budget information
def student_personalexp(student_name, rent, personal, groceries, insurance, entertainment, total_year, total_monthly):
    print(f'{student_name}\'s Budget:')
    print(f'Rent Fees: {rent}')
    print(f'Personal: {personal}')
    print(f'Groceries: {groceries}')
    print(f'Entertainment: {entertainment}')
    print(f'Insurance: {insurance}')
    print(f'Your total yearly expenses are: ${total_year}')
    print(f'Total monthly expenses are: ${total_monthly} ')


# Prints information
def display_info(nonstudent_name, annual_income, savings, total_year, expenses, total_deductions, total_monthly):
    print(f'{nonstudent_name}\'s Budget: ')
    print(f'Rent fees: ${expenses[0]}')
    print(f'Utilities: ${expenses[1]}')
    print(f'Personal: ${expenses[2]}')
    print(f'Insurance: ${expenses[3]}')
    print(f'Groceries: ${expenses[4]}')
    print()

    print(f'Annual income: ${annual_income}')
    print(f'Savings: ${savings}')
    print(f'Your total yearly expenses are: ${total_year}')
    print(f'Total monthly expenses are: ${total_monthly}')
    print(f'Your total after deductions are: ${total_deductions}')


def add_income():
    income = float(input("Enter your annual income: $"))
    return round(income, 2)


def add_savings():
    savings = float(input("Enter your current savings: $"))
    return round(savings, 2)


def add_rent():
    rent = -1
    while rent < 0:
        rent = float(input("Enter your monthly rent: $"))

    return round(rent, 2)


def add_utilities():
    cost = -1
    while cost < 0:
        cost = float(input("Enter your monthly utilities cost: $"))

    return round(cost, 2)


def add_personal():
    cost = -1
    while cost < 0:
        cost = float(input("Enter your monthly personal expenses: $"))

    return round(cost, 2)


def add_insurance():
    insurance = -1
    while insurance < 0:
        insurance = float(input("What is your monthly insurance payments: $"))

    return round(insurance, 2)


def add_groceries():
    groceries = -1
    while groceries < 0:
        groceries = float(input("What is your monthly groceries cost: $"))

    return round(groceries, 2)


def add_entertainment():
    entertainment = -1
    while entertainment < 0:
        entertainment = float(input("What is your monthly entertainment cost: $"))

    return round(entertainment, 2)


def print_stars():
    for _ in range(30):
        print('*', end='')
    print()


# Start of the program
# User inputs their name and determines if they are a student or not
name = input('Please enter name: ')
enrollment = input('Are you enrolled in Ryerson University[Y/N]: ')
if enrollment.lower() == 'y':
    student(name)
else:
    non_student(name)