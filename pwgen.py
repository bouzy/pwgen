#!/usr/bin/env python3

import string
import random

special_characters = list('~`!@#$%^&*()_-+={}[]|<>?')
lower_case = list(string.ascii_lowercase)
upper_case = list(string.ascii_uppercase)
digits = list(string.digits)
string_choice = lower_case + upper_case + digits + special_characters

passwd = []

def passwd_generator():
    random_loop = 0
    while random_loop < 21:
        passwd.append(random.choice(string_choice))
        random_loop += 1
    print(''.join(passwd))

if __name__ == '__main__':
    passwd_generator()
