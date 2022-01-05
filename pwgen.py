#!/usr/bin/env python3

import random

letters = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
special_characters = '~!@#$%^&*()_-+={}[]|<>?'
numbers = '0123456789'
string_choice = letters + special_characters + numbers
passwd = []

def passwd_generator():

    random_loop = 0

    while random_loop < 21:
        passwd.append(random.choice(string_choice))
        random_loop += 1
    
    print(''.join(passwd))

if __name__ == '__main__':
    passwd_generator()
