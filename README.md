# cblack

Custom Black Code Formatter for Python with 2-space indents

Same rules as Black, only with two-space indents.

## Installation

*cblack* can be installed by running `pip3 install cblack`.

It requires Python 3.6.0+ to run but you can reformat Python 2 code with it as well.

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

## Credits

All the credit is deserved to the people who created [black](https://github.com/ambv/black) on the first place.

Please visit black website:

- https://github.com/ambv/black
