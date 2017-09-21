# README

The README is a common file you'll find in data/code projects. Please, always read them. They are full of important information.

## Basic data analysis code structure

Here's how python code written to analyze data is usually structured:

- *Import necessary libraries/modules:* To use any code that isn't included in the base python, we need to import it at the top of our python file
- *Call the data:* In order to analyze the data you need to make python aware of it.
- *Do stuff to the data:* We do stuff to the data with functions. Functions can be things we write ourselves, or things that we call from the libraries/modules we import
- *Export the data:* Sometimes this means we bring in a csv file and export a smaller, more readable csv file. Sometimes this means we bring in a csv file and output a chart that makes the data easier to understand.

## Python concepts

There are some things you'll want to understand about python code... and code in general

- *No spaces. No special characters:* There are no spaces allowed in filenames or variable names or functions. If you put spaces in your file names now, you will stop after you start writing code. I promise you.
- *Variables:* Variables are a way of assigning data to short codes. For example, when I call data with agate, I'm creating a variable that I can reference to do further things with the data. A general rule of thumb with variables is to keep their names short, sweet and to the point.
```
my_data = agate.Table.from_csv('/path/to/data/file')
```
If I didn't use a variable, every time I wanted to do anything with my data, I'd have to call it again with `agate.Table.from_csv('/path/to/data/file')`. This wastes resources and time and it's ugly.
- *Functions:* Functions allow you to do the same set of things over and over again. Think of functions as assembly lines in a factory. A set of actions is performed the same way every time, over and over again. This saves time. Functions are declared with `def`.
```
def get_shit_done():
    my_data = agate.Table.from_csv('/path/to/data/file')
    print my_data
```
A general rule of thumb for functions is to name them with the action that they are set up to perform. For example, `get_shit_done()`.
- *Running python code:* To run python code, you simply call the file in your terminal or command prompt. 
`python analyze.py`






