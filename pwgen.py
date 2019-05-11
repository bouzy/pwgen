#!/usr/bin/python3.6

import random

passwd = []
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_case = 'abcdefghijklmnopqrstuvwxyz'
special_char = '!@#$%^&*()'
num_int = '1234567890'
str_choice = upper_case + lower_case + special_char + num_int

def pass_gen():
    loop = 0
    while loop < 30:
        passwd.append(random.choice(str_choice))
        loop += 1
    print(''.join(passwd))

if __name__ == '__main__':
    pass_gen()