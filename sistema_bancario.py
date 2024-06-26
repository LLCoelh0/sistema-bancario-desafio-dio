menu = '''
[D]eposit
[W]ithdraw
[S]tatement
[E]xit
Enter with a option: '''

balance = 0
limit = 500
statement = []
number_of_withdraws = 0
withdraw_limit = 3

while True:
    operation = input(menu).lower()

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
                if withdraw <= limit:
                    if balance - withdraw >= 0:
                        balance -= withdraw
                        statement.append(f'-U$ {withdraw:.2f}')
                        number_of_withdraws += 1
                    else:
                        print('Not enough balance, try other value')
                else:
                    print(f'Withdraw limit exceeded choose a value lower than {limit}')
            else:
                print('Enter with a valid value!')
        else:
            print('Number of withdraws exceeded for today!')

    elif operation == 's':
        if len(statement) == 0:
            print('No transactions were made')
        else:
            for number in statement:
                print(number)
        print(f'Balance U$ {balance:.2f}')

    elif operation == 'e':
        break

    else:
        print('Enter with a valid option')