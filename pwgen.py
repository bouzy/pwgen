#!/usr/bin/env python3

import string
import random

special_characters = list('~`!@#$%^&*()_-+={}[]|<>?')
lowercase_letters = list(string.ascii_lowercase)
uppercase_letters = list(string.ascii_uppercase)
digits = list(string.digits)
string_choice = lowercase_letters + uppercase_letters + digits + special_characters

def passwd_generator():
    passwd = []
    random_loop = 0
    while random_loop < 21:
        passwd.append(random.choice(string_choice))
        random_loop += 1
    print(''.join(passwd))

if __name__ == '__main__':
    passwd_generator()
