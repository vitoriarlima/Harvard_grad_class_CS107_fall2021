#!/usr/bin/python3


# Problem 3

#outer function, initial balance as argument
#inner function, withdrawal amount as an argument and return the balance

################Problem A

# CLOSURE:
#We must have a nested function (function inside a function).
#The nested function must refer to a value defined in the enclosing function.
#The enclosing function must return the nested function.

def make_withdrawal(balance):
    def withdrawal_amount(withdrawal):
        if withdrawal > balance:
            print('You dont have this availability in your bank account')
        if withdrawal < 0:
            print('Please add a positive amount for the withdrawal')
        else:
            new_balance = balance - withdrawal
            return new_balance
    return withdrawal_amount

#wd = make_withdrawal(init_balance)
#wd(withdrawal_amount)
#wd(new_withdrawal_amount)

wd = make_withdrawal(10)
print(wd(2)) 
print(wd(5))

# Explain why not it's working:
# The reason why both withdrawals are not updating is that the
# wd is referring only to the first balance amount on top, 
# i.e. the amount of balance = 10.
# Meaning, that it is not updating the balance.
# Hence the first withdrawal will show 8 and the
# second withdrawal will show 5, as if they started
# from two separate bank accounts with both initial balance of 10.

print("Explaining why not it's working:")
print("The reason why both withdrawals are not updating is that the wd is referring only to the first balance amount on top, i.e. the amount of balance = 10.")
print(" Meaning, that it is not updating the balance. Hence the first withdrawal will show 8 and the second withdrawal will show 5, as if they started from two separate bank accounts with both initial balance of 10.")
