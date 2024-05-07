balance = 0
statement = []
number_of_withdraws = 0
withdraw_limit = 3

while True:
    operation = input('''
[D]eposit
[W]ithdraw
[S]tatement
[E]xit
Enter with a option: ''').lower()
    
    if operation == 'd':
        deposit = float(input('Enter with the value for Deposit: '))
        if deposit <= 0:
            print('Enter with a valid value!')
        else:
            balance += deposit
            statement.append(f'+U$ {deposit:.2f}')

    elif operation == 'w':
        if number_of_withdraws < withdraw_limit:
            withdraw = float(input('Enter with the value for Withdraw: '))
            if withdraw > 0:
                if balance - withdraw >= 0:
                    balance -= withdraw
                    statement.append(f'-U$ {withdraw:.2f}')
                    number_of_withdraws += 1
                else:
                    print('Not enough balance, try other value')
            else:
                print('Enter with a valid value!')
        else:
            print('Number of withdraws exceeded for today!')

    elif operation == 's':
        for number in statement:
            print(number)
        print(f'Balance U$ {balance:.2f}')

    elif operation == 'e':
        break

    else:
        print('Enter with a valid option')