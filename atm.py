import random

def init():
    isValidOptionSelected = False
    print("Welcome to Green Bank")
    
    while isValidOptionSelected ==False:
        haveAccount = int(input("Do you have an account with us 1 - (Yes)  - 2 (No) \n"))    

        if haveAccount ==1:
            isValidOptionSelected = True
            login()
        elif haveAccount ==2:
            isValidOptionSelected = True
            register()
    else:
        print("You have selected an invalid option")
def bankOperation(user):
    print("Welcome %s %s" % (user[0], user[1]))
    
    selectedOption = int(input("""What would you like to do 
                                    1 - Deposit
                                    2 - Withdrawal
                                    3 - Logout \n"""))
    if selectedOption == 1:
        depositOperation()
    elif selectedOption == 2:
        withdrawalOperation()
    elif selectedOption == 3:
        login()
    elif selectedOption == 4:
        exit()
    else:
        print("Invalid option selected")
        bankOperation(user)

def generateAccountNumber():
    return random.range(1111111111,9999999999)

def depositOperation():
    print("THis is the deposit function")

def withdrawalOperation():
    print("This is the withdrawal Operation")

def login():
    print(("++++++++ Login +++++++++++"))
    
    isLoginSuccessful == False
    
    while isLoginSuccessful == False:
        
        accountNumberFromUser = int(input("What is your account number \n"))
        password = input("Enter your Password here \n")
        
        for accountNumberFromUser, userDetails in database.items():
            if accountNumber == accountNumberFromUser:
                if userDetails[3] == password:
                    isLoginSuccessful = True
                    
        print('Invalid account or password')
    bankOperation(userDetails)
    
    print("This is the login function")
    
def register():
    
    print("========= Register =========")
    
    email = input("What is your email address? \n")
    first_name = input("What is your first name \n")
    last_name = input("What is your last name")
    password = input("Type the password you would like to use \n")
    database[accountNumber] = [ first_name, last_name, email, password]
    
    print("Your Account has been created")
    print("Your account number is: %d" % accountNumber)
    print("Please keep it safe")
    accountNumber = generateAccountNumber()


init()
