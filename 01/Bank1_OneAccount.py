# Non-OOP
# Bank Version 1
# Single account

accountName = 'Joe'
accountBalance = 100
accountPassword = 'soup'

while True:
    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press w to make a withdrawal')
    print('Press s to show the account')
    print('Press q to quit')
    print()

    action = input('What do you want to do? ')
    action = action.lower()         # force lowercase
    action = action[0]              # just use first letter
    print()

    if action == 'b':
        print('Get Balance:')
        userPassword = input('\nPlease enter the password: ')
        if userPassword != accountPassword:
            print('Incorrect password')
        else:
            print('Your balance is:', accountBalance)

    elif action == 'd':
        print('Deposit:')
        userDepositAmount = input('\nPlease enter the amount to deposit: ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Please enter the password: ')

        if userDepositAmount < 0:
            print('You cannot deposit a negative amount!')

        elif userPassword != accountPassword:
            print('Incorrect password')

        else:                       # ok
            accountBalance = accountBalance + userDepositAmount
            print('Your new balance is:', accountBalance)

    elif action == 's':             # show
        print('Show:')
        print('       Name', accountName)
        print('       Balance:', accountBalance)
        print('       Password:', accountPassword)
        print()

    elif action == 'q':
        break

    elif action == 'w':
        print('Withdraw:')

        userWithdrawAmount = input('\nPlease enter the amount to withdraw:')

        userWithdrawAmount = int(userWithdrawAmount)
        userPassword = input('Please enter the password: ')

        if userWithdrawAmount < 0:
            print('You cannot withdraw a negative amount')

        elif userPassword != accountPassword:
            print('Incorrect password for this account')

        elif userWithdrawAmount > accountBalance:
            print('You cannot withdraw more than you have in your account')

        else:                          # ok
            accountBalance = accountBalance - userWithdrawAmount
            print('Your new balance is:', accountBalance)
print('Done')

