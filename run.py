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
