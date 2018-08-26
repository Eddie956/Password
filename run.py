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
    