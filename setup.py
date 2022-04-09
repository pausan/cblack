# Copyright (C) 2018 Pau Sanchez
import ast
import re
from setuptools import setup
import sys

assert sys.version_info >= (3, 7, 0), "cblack requires Python 3.7+"
from pathlib import Path  # noqa E402

CURRENT_DIR = Path(__file__).parent


def get_long_description() -> str:
  readme_md = CURRENT_DIR / "README.md"
  with open(readme_md, encoding="utf8") as ld_file:
    return ld_file.read()


def get_version() -> str:
  cblack_py = CURRENT_DIR / "cblack.py"
  _version_re = re.compile(r"__version__\s+=\s+(?P<version>.*)")
  with open(cblack_py, "r", encoding="utf8") as f:
    match = _version_re.search(f.read())
    version = match.group("version") if match is not None else '"unknown"'
  return str(ast.literal_eval(version))


setup(
    name="cblack",
    version=get_version(),
    description="The customized uncompromising code formatter.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    keywords="automation formatter black yapf autopep8 pyfmt gofmt rustfmt prettier",
    author="Pau Sanchez",
    author_email="contact@pausanchez.com",
    url="https://github.com/pausan/cblack",
    license="MIT",
    py_modules=["cblack"],
    packages=[],
    package_data={},
    python_requires=">=3.7.0",
    zip_safe=False,
    install_requires=["black==22.3.0"],
    extras_require={},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
    entry_points={"console_scripts": ["cblack=cblack:main"]},
)
