import sys

account_balance = float(500.25)  # starting Account balance

#functions ,balance, deposit and withdraw


def printbalance():
    print('Your current balance:\n{balance:.2f}'.format(
        balance=account_balance))


def deposit():
    global account_balance  # needs to be global to update global balance due to scope
    deposit_amount = float(
        input('How much would you like to deposit today?\n'))
    account_balance = account_balance + deposit_amount
    print('Deposit was ${deposit:.2f}, current balance is ${balance:.2f}'.format(
        deposit=deposit_amount, balance=account_balance))


def withdraw():
    global account_balance  # needs to be global to update global balance due to scope
    withdrawal_amount = float(
        input('How much would you like to withdraw today?\n'))
    if withdrawal_amount > account_balance:
        print('${withdrawal:.2f} is greater than your account balance of ${balance:.2f}'.format(
            withdrawal=withdrawal_amount, balance=account_balance))
    else:
        account_balance = account_balance - withdrawal_amount
        print('Withdrawal amount was ${withdrawal:.2f}, current balance is ${balance:.2f}'.format(
            withdrawal=withdrawal_amount, balance=account_balance))


userchoice = input("What would you like to do?\n")

if (userchoice == 'D'):  # deposit choice
    deposit()

elif userchoice == 'B':  # balance choice
    printbalance()


elif userchoice == 'W':  # withdrawal choice
    withdraw()

elif userchoice == 'Q':  # quits the program
    print('Thank you for banking with us.')
