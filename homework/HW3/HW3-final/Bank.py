#!/usr/bin/python3

######### Exercise 3 

#class BankAccount

from enum import Enum
class AccountType(Enum):
    SAVINGS = 1
    CHECKING = 2
    
#balance = 0

class BankAccount():
    
    def __init__(self, owner, accountType: AccountType):
        # your code
        self.balance = 0
        self.owner = owner
        self.accountType = accountType

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Withdrawal exceeds balance amount")
        elif amount < 0:
            raise ValueError("Withdrawal must be more than 0")
        else:
            self.balance = self.balance - amount
            return self.balance
            
    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Please enter a positive amount to deposit")
        else:
            self.balance = self.balance + amount
            return self.balance
            
        # your code

    def __str__(self):
        account_type = self.AccountType.name
        return "The owner of the given account is", self.owner,". The type of this account is a ", account_type, " account."
        # your code

    def __len__(self):
        #self.balance = self.balance + amount
        return self.balance
        # your code


######### PART B

class BankUser(BankAccount):
    
    def __init__(self, owner):
       # super().__init__(owner, AccountType)
        self.owner = owner
        self.accounts = []
        self.checkings = None
        self.savings = None
        #self.bankaccount = BankAccount(self.owner, AccountType)
    
    def addAccount(self, accountType):
        if accountType == AccountType.SAVINGS:
            if self.savings == None:
                self.savings = BankAccount(self.owner, AccountType)
                self.accounts.append(accountType.name)
            else:
                raise NameError("User has already a ", accountType.name , "type account")
                
        if accountType == AccountType.CHECKING:
            if self.checkings == None:
                self.checkings = BankAccount(self.owner, AccountType)
                self.accounts.append(accountType.name)
            else:
                raise NameError("User has already a ", accountType.name , "type account")
        # your code
        
        
    
    def getBalance(self, accountType):
        #bankaccount = BankAccount(self.owner, accountType)
                #self.bankaccount = BankAccount(self.owner, AccountType)
            if accountType == AccountType.SAVINGS:
                if self.savings == None:
                    raise NameError("You do not have a savings account, create one first.")
                return self.savings.balance #self.savings.__len__()
            if accountType == AccountType.CHECKING:
                if self.checkings == None:
                    raise NameError("You do not have a checking account, create one first.")
                return self.checkings.balance #self.savings.__len__()
            
            
        #return self.checkings.__len__()
        # your code
        
    def deposit(self, accountType, amount):
        #bankaccount = BankAccount(self.owner, accountType)
        if accountType == AccountType.SAVINGS:
            if self.savings == None:
                raise NameError("You do not have a savings account, create one first.")
            return self.savings.deposit(amount) #self.savings.__len__()
        if accountType == AccountType.CHECKING:
            if self.checkings == None:
                raise NameError("You do not have a checking account, create one first.")
            return self.checkings.deposit(amount) #self.savings.__len__()
        
        ##return accountType.deposit(amount)
        # your code

    def withdraw(self, accountType, amount):
        if accountType == AccountType.SAVINGS:
            if self.savings == None:
                raise NameError("You do not have a savings account, create one first.")
            return self.savings.withdraw(amount) #self.savings.__len__()
        if accountType == AccountType.CHECKING:
            if self.checkings == None:
                raise NameError("You do not have a checking account, create one first.")
            return self.checkings.withdraw(amount) #self.savings.__len__()
        #bankaccount = BankAccount(self.owner, accountType)
        ###return accountType.withdraw(amount)
        # your code

    def __str__(self):
        print("The owner of the given account is", self.owner,". These are the accounts of this client:")
        for account in self.accounts:
            return account



#########################

# PART C ATM

def ATMSession(user: BankUser):
   
    def Interface():
        while (True):
            print("Enter Option: \n"
                  "1)Exit \n"
                  "2)Create Account \n"
                  "3)Check Balance \n"
                  "4)Deposit \n"
                  "5)Withdraw . Your choice is")
            user_input = input()

            if user_input == "1":
                break


            ########## Creating account
            elif user_input == "2" : 
                print("Enter Option: \n"
                         "1) Checking \n"
                         "2) Savings \n")
                account = input()
                if account == "2":
                    #user = BankUser("Owner");
                    user.addAccount(AccountType.SAVINGS);
                    print(user.__str__())
                else:
                    user.addAccount(AccountType.CHECKING);
                    print(user.__str__())


            #############Checking the balance in the account
            elif user_input == "3" :
                print("Enter Option: \n"
                             "1) Checking \n"
                             "2) Savings \n")
                account = input()
                if account == "2":
                    #user = BankUser("Owner")
                    print(user.getBalance(AccountType.SAVINGS))


                else:
                    #user = BankUser("Owner")
                    print(user.getBalance(AccountType.CHECKING))      

            ########### Depositing or withdrawing
            elif user_input == "4" or user_input == "5":

                print("Enter Option: \n"
                             "1) Checking \n"
                             "2) Savings \n")
                account = input()
                print("Enter Integer Amount, Cannot be Negative:")
                new_user_input = int(input())

                ### 4 is deposit
                if user_input == "4" and account == "2":
                    #user = BankUser("Owner");
                    user.deposit(AccountType.SAVINGS, new_user_input)
                    print(user.getBalance(AccountType.SAVINGS))

                elif user_input == "4" and account == "1":
                    #user = BankUser("Owner");
                    user.deposit(AccountType.CHECKING, new_user_input)
                    print(user.getBalance(AccountType.CHECKING))

            ### 5 is withdrawing
                elif user_input == "5" and account == "2":
                    #user = BankUser("Owner");
                    user.withdraw(AccountType.SAVINGS, new_user_input)
                    print(user.getBalance(AccountType.SAVINGS))

                elif user_input == "5" and account == "1":
                    #user = BankUser("Owner");
                    user.withdraw(AccountType.CHECKING, new_user_input)
                    print(user.getBalance(AccountType.CHECKING));

    return Interface
                    
                   

##############################

def test_over_withdrawal(): #this test function should throw an Exception or Error 
    user = BankUser("Joe");
    user.addAccount(AccountType.SAVINGS);
    user.deposit(AccountType.SAVINGS, 20);
    print('Checking:', user.__str__())
    
    print("should be 10 and it is:", user.getBalance(AccountType.SAVINGS))
    try:
        
        user.withdraw(AccountType.SAVINGS, -2); #this will cause an Exception or Error
        print("it should still be 10", user.getBalance(AccountType.SAVINGS))
    except Exception as e:
        print(e); #print the message for the Exeption

test_over_withdrawal()

################################


# HERE I AM USING THE ATM SESSION #

#################

user = BankUser("Joe")
session = ATMSession(user)
session()

