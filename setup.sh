#!/bin/sh

pwgen_setup()
{
    chmod +x $script
    mkdir $directory_location
    cp $script $directory_location
    $symbolic_link
}

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    directory_location='/opt/pwgen'
    script='pwgen.py'
    symbolic_link='ln -s /opt/pwgen/pwgen.py /usr/bin/pwgen'
fi

if [[ "$OSTYPE" == "darwin"* ]]; then
    directory_location='/opt/pwgen'
    script='pwgen.py'
    symbolic_link='ln /opt/pwgen/pwgen.py /usr/bin/pwgen'
fi

pwgen_setup