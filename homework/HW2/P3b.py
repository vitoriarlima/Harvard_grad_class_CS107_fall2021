################Problem B

# CLOSURE:
#We must have a nested function (function inside a function).
#The nested function must refer to a value defined in the enclosing function.
#The enclosing function must return the nested function.

def make_withdrawal(balance):
    def withdrawal_amount(withdrawal):
        #nonlocal balance 
        if withdrawal > balance:
            print('You dont have this availability in your bank account')
        if withdrawal < 0:
            print('Please add a positive amount for the withdrawal')
        else:
            #new_balance = balance - withdrawal
            balance = balance - withdrawal
            #return new_balance
            return balance

    return withdrawal_amount

#wd = make_withdrawal(init_balance)
#wd(withdrawal_amount)
#wd(new_withdrawal_amount)

wd = make_withdrawal(10)
wd(2) 
wd(5)

# Explanation:
# It is not working because balance here is not a nonlocal variable.
# Here I can reference it, but still I am not updating it, which is what I want.