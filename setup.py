import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'clexography',
    version = 'v0.2.5',
    scripts = ['clexography'] ,
    author = "clexography",
    author_email = "exotech.code@gmail.com",
    description = "Image to text converter and vice versa.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/eXotech-code/clexography",
    py_modules = ['functions'],
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
