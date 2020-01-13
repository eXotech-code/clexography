#!/bin/sh

echo Starting installation of clexography...
echo -e "Checking if pip is installed...\n"
command -v pip3 >/dev/null 2>&1 || continue
command -v pip >/dev/null 2>&1 || { echo >&2 "Pip not found on this system. Please install pip and try again."; exit 1; }
echo Pip has been found. continuing...
echo -e "Creating a python package...\n"
python3 setup.py sdist bdist_wheel
echo Package has been created.
echo -e "Installing package...\n"
sudo pip install ./dist/clexography-0.2-py3-none-any.whl
echo -e "\nClexography has been succesfully installed. Goodbye!"
