#!/bin/sh

directory_location='/opt/pwgen'
script='pwgen.py'
symbolic_link='ln -s /opt/pwgen/pwgen.py /usr/bin/pwgen'

pwgen_setup()
{
    chmod +x $script
    mkdir $directory_location
    cp $script $directory_location
    $symbolic_link
}

pwgen_setup