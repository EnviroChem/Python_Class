import random

database = {}

allowedUsers = ['Seyi', 'Bill', 'Laura']
allowedPassword = ['passSeyi', 'passBill', 'passLaura']
acctBalance = [8000, 6000, 5000] #accntNumber =

def init():
    print("===================================================")
    print(' Welcome to Environmental Bank of Maryland!')
    
    import datetime
    now = datetime.datetime.now()
    print(now.strftime("            %Y-%m-%d %H:%M:%S"))
    print("================== ATM Main Menu ==================")
    print(" 1. Login")
    print(" 2. Register for a new bank account")
    print("===================================================")
    haveAccount = int(input("Please select an option from the numbers above \n"))
    
    if(haveAccount == 1):
        login()

    elif(haveAccount == 2):
        print(" Thank you for choosing to open a new account with us!")
        print(' Lets get started!')
        register()

    else:
        print(' Incorrect selection, lets return to the main screen.')
        init()


def login():
    print('=============== Login ===============')
    
    name = input(" Please input your Login name: \n")
    while(name not in allowedUsers):
        print('Name not found, please try again')
        name = input(" Please input your Login name: \n")
        
    password = input(" Please enter your password? \n")
    userID = allowedUsers.index(name)

    while(password != allowedPassword[userID]):
        print(" Password Incorrect, please try again")
        password = input(" Please enter your password: \n")

    if(password == allowedPassword[userID]):
        mainMenu()
                
    print(" Invalid account or password, now returning to the main menu")
    init()
    
def register():
    print("********** New Member Registration **********")
    
    email = input(" Please provide your E-mail address? \n")
    first_name = input(" What is your first name? \n")
    last_name = input(" What is your last name? \n")
    password = input(" Please create a password for your account \n")
    
    accntNumber = generateAccountNumber()
    
    database[accntNumber] = [ first_name, last_name, email, password ]

    print(" Your New Account has been Successfully created!")
    print("============ === =========== ===== =======")
    print(" Your account number is: %d" % accntNumber)
    print(" Make sure to write down your account number")
    print("Would you like to return to the main menu?")
    print(" 1. Yes")
    print(" 2. No")
    returnz = int(input("Please enter a number from the list above \n"))
    if(returnz == 1):
        print("Now returning to the Main menu")
        init()
    elif(returnz == 2):
        print('Thanks for visiting! Now exiting the system')
        init()
    else:
        print('Invalid selection, now returning to main menu')
        init()
        
    
def mainMenu():
    
    print('Welcome %s' % allowedUsers )
    print('What business do you have with us today?')
    print('1. Withdrawal')
    print('2. Cash Deposit')
    print('3. Check Account Balance')
    print('4. Complaint')

    selectedOption = int(input('Please choose a number from the options above: \n'))

    if(selectedOption == 1):
    
        print('========== Withdrawal menu ==========')
        currentBalance = str(acctBalance)
        print(' Your current balance is : $' + str(currentBalance))
        withdrawal = int(input(' How much would you like to withdraw? \n'))
        
        print(' Please take your cash from the tray below')
        print('=====================================')
        returnMenu()

        
    elif(selectedOption == 2):
    
        print('========== Deposit menu ==========')
        deposit = int(input('How much would you like to deposit? \n'))
        currentBalance = (acctBalance)
        newBalance = str(currentBalance + deposit)
        print('Your new balance is: $' + newBalance)
        returnMenu()
        

    elif(selectedOption == 3):

        print('========== Account Balance menu ==========')
        #userBalance = allowedUsers.index)
        currentBalance = (acctBalance[userID])
        print('Your current account balance is: $' + str(currentBalance))
        returnMenu()

        
    elif(selectedOption == 4):

        print('========== Complaint submission ==========')
        print('We highly value feedback from our customers')
        print('Please follow the prompt below to submit a complaint')
        issue = input('What issue would you like to report? (word limit: 300 words) \n')
        print('We have recieved your complaint and will respond within 1 to 5 business days.')
        print('Thank you very much for contacting us!')
        returnMenu()

    else:
        print('Invalid option selected, please try again')
        mainMenu()

#def withdrawalOption():
    

#def depositOption():
    

#def chkAccountBalance():
    

def returnMenu():
    print('Would you like to complete another transaction?')
    print(' 1. Yes -- Return to the Main menu')
    print(' 2. No -- To return your ATM card and Logout')
    returnMain = int(input('Please select from the options listed above \n'))

    if(returnMain == 1):
        mainMenu()

    elif(returnMain == 2):
        print('=====================================')
        print('Thank you for your business today!')
        print('Please remember to take your bank card and belongings')
        print('We will see you again soon!')
        print('=====================================')
        logout()

    else:
        print("Invalid selection, now returning to the Main menu")
        returnMenu()

#def complaintOption():
    

def generateAccountNumber():

    return random.randrange(11111111,99999999)

def logout():
    print('Now returning to the main screen')
    init()

#ACTUAL BANK SYSTEM

init()  
