checking = 70000  # initial balance
deposit_count = 4  # max deposit frequency
withdrawal_count = 3  # max withdrawal frequency counter
max_deposit = 40000  # max deposit per transaction
max_depositday = 150000  # max deposit for the day
max_withdr = 20000  # max withdrawal per transaction
max_withdrday = 50000  # max withdrawal for the day


def main_menu():
    print("WELCOME TO TALA ATM")
    print("""
    --------------------------
    Select service:
    1. Show my current balance
    2. Deposit cash
    3. Cash Withdrawal
    4. Quit
    --------------------------
    """)
    option = None
    while option != 4:
        option = int(input("Enter option: "))
        if option == 1:
            balance()
        elif option == 2:
            deposit()
        elif option == 3:
            withdrawal()
        elif option == 4:
            quit()
        else:
            print("""
            -------------------------------
            Please enter option from 1 to 4
            -------------------------------
            """)


def balance():
    print("""
    ---------------------------------

    You current balance is $ """, checking,
          """
           ---------------------------------
           """)
    main_menu()


def deposit():
    global checking
    global deposit_count
    global max_deposit
    global max_depositday

    money = int(input("Enter deposit amount: "))
    if money <= max_deposit and deposit_count != 0 and money < max_depositday:
        checking += money
        deposit_count -= 1
        max_depositday -= money
        balance()
    elif money > max_deposit:
        print("""
        -----------------------------------------------
        You cannot deposit more than 40k at one time
        -----------------------------------------------
        """)
    elif money > max_depositday:
        print("""
        ---------------------------------------------
        You cannot deposit more than 150k for the day
        ---------------------------------------------
        """)
    else:
        print("""
        ---------------------------------------------
        You exceeded your daily deposit frequency
        ---------------------------------------------
        """)
    main_menu()


def withdrawal():
    global checking
    global withdrawal_count
    global max_withdrday
    global max_withdr

    money = int(input("Enter withdrawal amount: "))
    if money <= checking and money <= max_withdrday and withdrawal_count != 0 and money <= max_withdr:
        checking -= money
        withdrawal_count -= 1
        max_withdrday -= money
        balance()
    elif money > max_withdrday:
        print("""
        -------------------------------------------
        You cannot withdraw more than 50k for the day
        --------------------------------------------
        """)
    elif money > max_withdr:
        print("""
        ---------------------------------------------
        You cannot withdraw more than 20k at one time
        ---------------------------------------------
        """)
    elif money > checking:
        print("""
        ---------------------------------------------
        You don't have enough money on your account
        --------------------------------------------
        """)
    else:
        print("""
        --------------------------------------------
        You exceeded your daily withdraw frequency
        -------------------------------------------
        """)
    main_menu()


def quit():
    response = None
    global checking
    while response != "Y" and response != "N":
        response = str(input("Do you want to quit? press Y or N: "))
    if response == "Y":
        checking = 0
        print("Good Bye!")
        exit()
    else:
        main_menu()


main_menu()
