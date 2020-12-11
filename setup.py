#!/usr/bin/python3

from os import system as terminal

directory_location = '/opt/pwgen/'
script = 'pwgen.py'
symbolic_link = 'ln -s /opt/pwgen/pwgen.py /usr/bin/pwgen'

def pwgen_setup():
    terminal('chmod +x ' + script)
    terminal('mkdir ' + directory_location)
    terminal('cp ' + script + ' ' + directory_location)
    terminal(symbolic_link)

if __name__ == "__main__":
    pwgen_setup()
