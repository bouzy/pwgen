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
    while random_loop < 21:
        passwd.append(random.choice(string_choice))
        random_loop += 1
    validation()

def validation():
    digit = 'no'
    special_character = 'no'
    lowercase = 'no'
    uppercase = 'no'
    exitcode = 'FAILED'
    
    for p in passwd:
        if p in digits and digit == 'no':
            #print(p + ' is a digit')
            digit = 'yes'
        elif p in special_characters and special_character == 'no':
            #print(p + ' is a special character')
            special_character = 'yes'
        elif p in lowercase_letters and lowercase == 'no':
            #print(p + ' is a lowercase character')
            lowercase = 'yes'
        elif p in uppercase_letters and uppercase == 'no':
            #print(p + ' is an uppercase character')
            uppercase = 'yes'

        if special_character == 'yes' and lowercase == 'yes' and uppercase == 'yes' and digit == 'yes':
            exitcode = 'PASSED'
        else:
            exitcode = 'FAILED'
    
    if exitcode == 'PASSED':
        print(''.join(passwd))
        return
    else:
        passwd_generator()

if __name__ == '__main__':
    validation()