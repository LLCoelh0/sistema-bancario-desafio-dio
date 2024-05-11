import os

balance = 0.0
limit = 500
statement = []
number_of_withdraws = 0
withdraw_limit = 3

def deposit(balance, statement):
    deposit_value = float(input('\n Enter with the value for Deposit: '))
    if deposit_value <= 0:
        print('Enter with a valid value!')
    else:
        balance += deposit_value
        statement.append(f'+U$ {deposit_value:.2f}')
    return balance

def withdraw(limit, statement, balance, number_of_withdraws, withdraw_limit):
    if number_of_withdraws < withdraw_limit:
        withdraw = float(input('\n Enter with the value for Withdraw: '))
        if withdraw > 0:
            if withdraw <= limit:
                if balance - withdraw >= 0:
                    balance -= withdraw
                    statement.append(f'-U$ {withdraw:.2f}')
                    number_of_withdraws += 1
                else:
                    print('\n Not enough balance, try other value')
            else:
                print(f'\n Withdraw limit exceeded choose a value lower than {limit}')
        else:
            print('\n Enter with a valid value!')
    else:
        print('\n Number of withdraws exceeded for today!')
    return balance, number_of_withdraws

def print_statement(balance, /, statement):
    if len(statement) == 0:
        print('\nNo transactions were made')
    else:
        for number in statement:
            print(number)
    print(f'Balance U$ {balance:.2f}')
    input("\n\n Press Enter to continue...")

menu = '''
[D]eposit
[W]ithdraw
[S]tatement
[E]xit
Enter with a option: '''

while True:
    os.system('clear')
    operation = input(menu).lower()
    if operation == 'd':
        balance = deposit(balance, statement)
    elif operation == 'w':
        balance, number_of_withdraws = withdraw(limit=limit, statement=statement, balance=balance, number_of_withdraws=number_of_withdraws, withdraw_limit=withdraw_limit)
    elif operation == 's':
        print_statement(balance, statement=statement)
    elif operation == 'e':
        break
    else:
        print('Enter with a valid option')