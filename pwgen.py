#!/usr/bin/python3.6

import random

passwd = []
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_case = 'abcdefghijklmnopqrstuvwxyz'
special_char = '!@#$%^&*()'
number = '0123456789'
str_choice = upper_case + lower_case + special_char + number

def pass_gen():
    rand_loop = 0
    while rand_loop < 30:
        passwd.append(random.choice(str_choice))
        rand_loop += 1
    print(''.join(passwd))

if __name__ == '__main__':
    pass_gen()