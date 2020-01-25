#!/bin/sh

# installation function
install() {
    echo Pip has been found. continuing...
    echo -e "Installing setup tools...\n"
    sudo python3 -m pip install --upgrade pip setuptools
    sudo python3 -m install --upgrade wheel
    echo -e "Creating a python package...\n"
    python3 setup.py sdist bdist_wheel
    echo Package has been created.
    echo -e "Installing package...\n"
    sudo pip3 install ./dist/clexography-0.3-py3-none-any.whl
    echo -e "\nClexography has been succesfully installed. Goodbye!"
}

echo Starting installation of clexography...
echo -e "Checking if pip is installed...\n"
if hash pip 2>/dev/null; then
    install
elif hash pip3 2>/dev/null; then
    install
else
    read -p "Pip not found on this system. Do you want to install it? (Y/n)" confirm
    if [ $confirm = Y -o $confirm = y -o $confirm = yes -o $confirm = Yes ]; then
        sudo apt install python3-pip
    elif [ $confirm = N -o $confirm = n -o $confirm = no -o $confirm = No]; then
        echo Pip will not be installed. Aborting...
    else
        echo -e "This is not a valid command. Aborting..."
    fi
fi