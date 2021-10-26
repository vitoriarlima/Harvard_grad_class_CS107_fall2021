#!/usr/bin/python3

## test each error
# withdraw more than balance

import Bank


def test_over_withdrawal_s():
    user = BankUser("Joe");
    user.addAccount(AccountType.SAVINGS);
    user.deposit(AccountType.SAVINGS, 10);
    #print(user.__str__())
    
    #print("User balance", user.getBalance(AccountType.SAVINGS))
    try:
        user.withdraw(AccountType.SAVINGS, 1000); #this will cause an Exception or Error
    except Exception as e:
        print(e); #print the message for the Exeption

def test_over_withdrawal_c():
    user = BankUser("Joe");
    user.addAccount(AccountType.CHECKING);
    user.deposit(AccountType.CHECKING, 10);
    #print(user.__str__())
    
    #print("User balance", user.getBalance(AccountType.SAVINGS))
    try:
        user.withdraw(AccountType.CHECKING, 1000); #this will cause an Exception or Error
    except Exception as e:
        print(e);

test_over_withdrawal_s()
test_over_withdrawal_c()


# withdrawal less than 0
def test_under_withdrawal_s():
    user = BankUser("Joe");
    user.addAccount(AccountType.SAVINGS);
    user.deposit(AccountType.SAVINGS, 10);
    #print(user.__str__())
    #print("User balance", user.getBalance(AccountType.SAVINGS))
    try:
        user.withdraw(AccountType.SAVINGS, -1); #this will cause an Exception or Error
    except Exception as e:
        print(e); #print the message for the Exeption

def test_under_withdrawal_c():
    user = BankUser("Joe");
    user.addAccount(AccountType.CHECKING);
    user.deposit(AccountType.CHECKING, 10);
    #print(user.__str__())
    #print("User balance", user.getBalance(AccountType.SAVINGS))
    try:
        user.withdraw(AccountType.CHECKING, -1); #this will cause an Exception or Error
    except Exception as e:
        print(e); #print the message for the Exeption

test_under_withdrawal_s()
test_under_withdrawal_c()

# Test zero deposit
def test_under_deposit_s():
    user = BankUser("Joe");
    user.addAccount(AccountType.SAVINGS);
    #print(user.__str__())
    #print("User balance", user.getBalance(AccountType.SAVINGS))
    try:
        user.deposit(AccountType.SAVINGS, -1) #this will cause an Exception or Error
    except Exception as e:
        print(e); #print the message for the Exeption

def test_under_deposit_c():
    user = BankUser("Joe");
    user.addAccount(AccountType.CHECKING)
    #print(user.__str__())
    #print("User balance", user.getBalance(AccountType.SAVINGS))
    try:
        user.deposit(AccountType.CHECKING, -1) #this will cause an Exception or Error
    except Exception as e:
        print(e); #print the message for the Exeption

test_under_deposit_s()
test_under_deposit_c()

# Test add account savings
def test_add_account_savings():
    user = BankUser("Joe");
    user.addAccount(AccountType.SAVINGS)
    #print(user.__str__())
    #print("User balance", user.getBalance(AccountType.SAVINGS))
    try:
        user.addAccount(AccountType.SAVINGS); #this will cause an Exception or Error
    except Exception as e:
        print(e); #print the message for the Exeption

# Add Checking Account
def test_add_account_checking():
    user = BankUser("Joe");
    user.addAccount(AccountType.CHECKING)
   
    try:
        user.addAccount(AccountType.CHECKING) #
    except Exception as e:
        print(e);
        
test_add_account_checking()
test_add_account_savings()

def test_no_account():
    user = BankUser("Joe");
    user.withdraw(AccountType.CHECKING,10); #
test_no_account()
