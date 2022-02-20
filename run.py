#!/usr/bin/env python3.9
from user import User
import getpass
import random
import string
dash = '-' * 60


def create_account(account_name,username,password,confirm_password):

    """
    function to create a new account
    """

    new_user = User(account_name,username,password,confirm_password)

    return new_user

def save_details(user):

    """
    function to save save_details
    """
    user.save_detail()

def display_all_details():

    """
    function used to return all saved save_details
    """
    return User.display_all_details()

def check_existing_user(username):

    """
    a function that is used to check and return all exissting accounts
    """

    return User.user_exist(username)

def find_user(username):

    """
    the function is used check details from the saved save_details
    """

    return User.find_by_username(username)

def generatePassword(num):
   genpas = ''

   for n in range(num):
       x = random.randint(0,94)
       genpas += string.printable[x]

   return genpas

def main():
    print('{:_^5}'.format('PASSWORD LOCKER, no need to write down your passwords!!'))

    print('\n')
    print('{:_^10}'.format('LOGIN'))
    print('\n')
    print("hi there, please supply your name")
    user_name= input().upper()
    print(f"Hello {user_name},welcome to password manager, what would you like to do?")
    print("\n")
    
    while True:
        list=('''
        na-Register a new account
        da-display accounts
        fa-Find accounts
        ex-Exit\n''')
        print(list)

        short_code= input().lower()

        if short_code == 'na':
            print (f"{user_name} please fill in the following fields:")
            print ("_"*7)
            print ("Account Name")
            account_name = input()
            print ('\n')

            print("Username")
            username= input()
            print('\n')

            print("Please supply your password..")
            password=getpass('password:')
            print("********")
            confirm_password = getpass('password:')
            print('********')
            save_details(create_account(account_name,username,password,confirm_password))
            print('\n')

            print(dash)
            print('\n')
            print(f'{user_name} please enter te short codes to continue..')

        elif short_code=='da':
            if display_all_details():
                print(f"{user_name} below is all your accounts")
                print('\n')

                for user in display_all_details():
                    print(dash)

                    print(f'Account is {user.account_name}.com')
                    print(f'Account username is {user.username}.')
                    print(f'Your account password is {user.password}. Keep your passwords always safe.')
                    print(dash)
                    print('\n')
                    print(f'{user_name} please enter te short codes to continue..')


        elif short_code =='fa':
            print(f'{user_name}, enter the username you want to search for..')
            search_username= input()

            if check_existing_user(search_username):
                 search_username= find_user(search_username)
                 print(dash)
                 print(f'Account is {search_username.account_name}.com')
                 print(f'Account username is {search_username.username}')
                 print(f'Account password is {search_username.password}Keep your passwords safe')
                 print(dash)
                 print(f'{user_name} please enter te short codes to continue..')

            else:
                print(f'{user_name} That account does not exist, please search again')
                print(f'{user_name} please enter te short codes to continue..')
        
        elif short_code == "ex":
             print("Goodbye and dont foret to rate our app..")
             break
        else :
            print("Please use correct code")
            print(f'{user_name} please enter te short codes to continue..')

