# cblack

Custom Black Code Formatter for Python with 2-space indents

Same rules as Black, only with two-space indents.

## Installation

*cblack* can be installed by running `pip3 install cblack`.

It requires Python 3.7+ to run but you can reformat Python 2 and Python 3.x code
as well (although you should run cblack with a Python 3.7+ interpreter).

NOTE: Running cblack with Python 3.6 is no longer supported since black itself
is failing as well.

## Usage

    python -m cblack {source_file_or_directory}

## Options

    python -m cblack --help

You can also go to https://github.com/psf/black for the latest options available

## Why

After [a long discussion](https://github.com/ambv/black/issues/378) about indentation
levels it was decided by the main author that:

    Two space indents are not distinct enough to be recommended by the Black coding style.

The whole pourpose of this project is to provide an alternative to black, with
the exact same rules and behaviour, but using 2 spaces for indentation instead of 4.
All other black options are still supported.

Second reason is that [Google YAPF](https://github.com/google/yapf) is not able
to produce same output as black (mostly because of function arguments indentation),
otherwise, if it was possible to do it, I would not have created this project.

## How

I'm a busy man. I don't want to spend my time pulling latest changes from black
regularly, so I've created a small package that depends on black and overrides
a method to reindent using two spaces. Shall black developers break this behaviour
I might end up cloning the whole project. But the aim of this project
would still be the same.

## Similar projects

- YAPF
- Autopep8
- pep8ify
- pyfmt
- prettier in node
- gofmt in go
- rustfmt in rust

## Versioning

This project will try to follow the same versioning as black itself, so any
changes introduced in black formatting will be reflected in this project as well.

As black project states:

     This is made explicit by the “Beta” trove classifier, as well as by 
     the “b” in the version number. What this means for you is that until
     the formatter becomes stable, you should expect some formatting to change
     in the future.


## Credits

All the credit is deserved to the people who created [black](https://github.com/ambv/black) on the first place.

Please visit black website:

- https://github.com/ambv/black
