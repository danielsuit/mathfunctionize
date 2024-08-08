from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'Set of functions to perform mathematical operations.'
LONG_DESCRIPTION = 'A package that allows you to perform advanced mathematical operations.'

# Setting up
setup(
    name="mathfunctionize",
    version=VERSION,
    author="Daniel Suit",
    author_email="<ds8ds8ds8@outlook.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['math', 'mathematics', 'function', 'functions', 'topology', 'algebra'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
