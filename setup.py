#!/usr/bin/python3.6

from os import system as terminal

# PLACEMENT
directory_location = '/opt/pwgen/'
scripts = 'pwgen.py'
terminal_command = 'ln -s /opt/pwgen/pwgen.py /usr/bin/pwgen'

def pwgen_setup():
    terminal('mkdir ' + directory_location)
    terminal('cp ' + scripts + ' ' + directory_location)
    terminal(terminal_command) #SYMBOLIC LINK IS BROKEN

if __name__ == "__main__":
    pwgen_setup()