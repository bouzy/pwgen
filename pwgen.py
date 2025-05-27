#!/usr/bin/env python3

import string
import random

digits = list(string.digits)
special_characters = list(string.punctuation)
lowercase_letters = list(string.ascii_lowercase)
uppercase_letters = list(string.ascii_uppercase)
string_choice = digits + special_characters + lowercase_letters + uppercase_letters

passwd = []

def passwd_generator():
    random_loop = 0
    while random_loop < 25:
        passwd.append(random.choice(string_choice))
        random_loop += 1
    validation()

def validation():
    digit = 'no'
    special_character = 'no'
    lowercase = 'no'
    uppercase = 'no'
    
    for password in passwd:
        if password in digits and digit == 'no':
            digit = 'yes'
        elif password in special_characters and special_character == 'no':
            special_character = 'yes'
        elif password in lowercase_letters and lowercase == 'no':
            lowercase = 'yes'
        elif password in uppercase_letters and uppercase == 'no':
            uppercase = 'yes'

        if special_character == 'yes' and lowercase == 'yes' and uppercase == 'yes' and digit == 'yes':
            exitcode = 'PASSED'
        else:
            exitcode = 'FAILED'

    if exitcode == 'PASSED':
        print(''.join(passwd))
        return
    else:
        passwd.clear()
        passwd_generator()

if __name__ == '__main__':
    passwd_generator()