import os
import requests
from pprint import pprint

def menu():       
    menu = '''
    [C]reate a Client
    [G]enerate account
    [A]ccounts
    [L]ist Clients
    [D]eposit
    [W]ithdraw
    [S]tatement
    [E]xit
    Enter with a option: '''

    return input(menu)

def create_customer(clients):

    cpf = input('\nEnter with the customer cpf(only numbers): ')
    if cpf in clients:
        print('\n Client already exist!')
        input("\n\n Press Enter to continue...")
    else:
        customer = {cpf :{'name':'null', 'date_of_birth':'null', 'adress':{'street':'street','number':0, 'district':'null', 'city':'city', 'state':'state' }}}
        customer[cpf]['name'] = input('\nEnter with the name of the client: ')
        customer[cpf]['date_of_birth'] = input('\nEnter with date of birth(separatede by /): ')

        cep = input('\nEnter with the client CEP(only number): ')

        if len(cep) == 8:

            link = f'https://viacep.com.br/ws/{cep}/json/'
            requisicao = requests.get(link)
            dic_requisicao = requisicao.json()

            customer[cpf]['adress']['state'] = dic_requisicao['uf']
            customer[cpf]['adress']['city'] = dic_requisicao['localidade']
            customer[cpf]['adress']['district'] = dic_requisicao['bairro']
            customer[cpf]['adress']['street'] = dic_requisicao['logradouro']
        else:
            print("CEP Inválido")
        
        customer[cpf]['adress']['number'] = input('\nEnter with the residence number: ')
        clients.update(customer)

def deposit(balance, statement):

    deposit_value = float(input('\n Enter with the value for Deposit: '))
    if deposit_value <= 0:
        print('Enter with a valid value!')
    else:
        balance += deposit_value
        statement.append(f'+U$ {deposit_value:.2f}')
    return balance

def withdraw(*, limit, statement, balance, number_of_withdraws, withdraw_limit):

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
                    input("\n\n Press Enter to continue...")
            else:
                print(f'\n Withdraw limit exceeded choose a value lower than {limit}')
                input("\n\n Press Enter to continue...")
        else:
            print('\n Enter with a valid value!')
            input("\n\n Press Enter to continue...")
    else:
        print('\n Number of withdraws exceeded for today!')
        input("\n\n Press Enter to continue...")
    return balance, number_of_withdraws

def print_statement(balance, /, *, statement):

    if len(statement) == 0:
        print('\nNo transactions were made')
    else:
        for number in statement:
            print(number)
    print(f'Balance U$ {balance:.2f}')
    input("\n\n Press Enter to continue...")

def create_account(clients, agency, account_number):

    cpf = input('Enter with the cpf of the client: ')

    if cpf in clients:
        return {'client':cpf, 'agency': agency, 'account_number':account_number}
    else:
        print('Client dos not exist!')
        input("\n Press Enter to continue...")
        return None

def main():

    balance = 0.0
    limit = 500
    statement = []
    number_of_withdraws = 0
    withdraw_limit = 3
    clients = {}
    agency = '0001'
    account_number = 0
    accounts = []

    while True:
        os.system('clear')
        operation = menu().lower()
        if operation == 'c':
            create_customer(clients)

        elif operation == 'g':
            account_number = len(accounts)+1
            account = create_account(clients, agency, account_number)
            accounts.append(account)

        elif operation == 'l':
            pprint(dict(clients))
            input("\n\n Press Enter to continue...")
        
        elif operation == 'a':
            for acc in accounts:
                print(acc)
            input("\n\n Press Enter to continue...")
        
        elif operation == 'd':
            balance = deposit(balance, statement)
        
        elif operation == 'w':
            balance, number_of_withdraws = withdraw(limit=limit, statement=statement, balance=balance, number_of_withdraws=number_of_withdraws, withdraw_limit=withdraw_limit)
        
        elif operation == 's':
            print_statement(balance, statement=statement)
        
        elif operation == 'e':
            break
        
        else:
            print('Enter with a valid option')

main()