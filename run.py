#!/usr/bin/env python3.6
import pyperclip
from credential import User,Credential

def create_user(f_name,l_name,password):
    '''
    function that create a new user
    '''
    new_user = User(f_name,l_name,password)
    return new_user

def save_user(user):
    '''
    saving a new user acount
    '''
    User.save_user(user)

def generate_password():
    '''
    to generate a password automaticaly
    '''
    generate_password = Credential.generate_password()
    return generate_password

def create_credential(user_name,account_name,password):
    '''
    function to create a new credential
    '''
    new_credential=Credential(user_name,account_name,password)
    return new_credential

def save_credential(credential):
    '''
    functions to save credentials
    '''
    Credential.save_credential(credential)

def display_credential(user_name):
    '''
    function to display credential saved by a user
    '''
    return Credential.display_credential(user_name)

def copy_credential(account_name):
    '''
    function to copy credential details in a clipboard
    '''
    return Credential.copy credential(account_name)

def main():
    print("Hello Welcome to Password locker.what is your name?")
    user_name = input()
    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while Ttrue:
        print("use these short codes : ca - create account, lg - login, dc - display credential, fc - find credential, ex - exit")

        short_code = input().lower()
        if short_code == 'ca':
            print('Create a new account:')
            f_name = input('Enter your first name -').strip()
            l_name = input('Enter your last name -').strip()
            password = ('Enter your password - ').strip()
            save_user(create_user(f_name,l_name,password))
            print("\n")
            print(f"New Account Created for: {f_name} ")
        
        elif short_code == 'lg':
            print("Please login to your acount:")
            user_name = input('Enter your first name - ').strip()
            password = str(input('Enter your password - '))
            user_exists = verify_user(user_name,password)
            if user_exists == user_name:
                print("\n")
                print("Welcome {user_name}. What do you want to do")
                
                while True:
                    print
                
