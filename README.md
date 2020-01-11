# clexography
Clexography is a tool used to convert image files to and from text.

It can be used for example as a way of sending images over IRC chat or anywhere else, where you cannot send images normally.

### Branches
[master](https://github.com/eXotech-code/clexography/tree/master) -  Main production branch

[testing](https://github.com/eXotech-code/clexography/tree/testing) - This branch always lags behind master a little bit. It contains finished code not yet ready to merge with master (merges occur every week)

[feature](https://github.com/eXotech-code/clexography/tree/feature) - Branch with new, untested features


### Usage
#### Installation
To use clexography you need to have Python3 installed.

There is no need for any additional dependencies.

Just clone the repo, open it in terminal and type in:

`python3 setup.py sdist bdist wheel`

`sudo pip install ./dist/clexography-0.2-py3-none-any.whl`

Or if you want the easier way. Grab one of our newest [binaries](https://github.com/eXotech-code/clexography/releases) and run on it:

`sudo pip install clexography-0.2-py3-none-any.whl`

###### Python3 intallation
[It's right here!](https://wiki.python.org/moin/BeginnersGuide/Download)

#### Running
Run by typing in the console

To generate text from image file:
`./clexography -e path-to-the-image-file.jpg path-to-save-text-file.txt`

To decode image from text file:
`./clexography -d path-to-the-text-file.txt path-to-save-image-file.jpg`

##### You can do whatever you want with this code.

If you want, you can upstream your changes in feature branch :)
