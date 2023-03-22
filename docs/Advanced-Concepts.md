# Advanced Concepts

[< back to specs](./)

***This section of the spec is completely optional.*** The Creative AI Project contains a lot of code and concepts that you are not expected to understand to complete the project. However, many of these details are interesting or useful. This section is for explaining them.

## Table of Contents

- [Exceptions](#exceptions)
- [Magic Methods](#magic-methods)

## Magic Methods

Like C++, Python allows users to overwrite operators for custom class definitions. Python, however, uses many fewer words to achieve much more. As an example consider trying to print out an instance of a Point object with x and y coordinates. In C++ that would look something like this:

```
ostream& operator<< (ostream& outs, Point pt)
{
    outs << "(" << pt.x << "," << pt.y << ")";
    return outs;
}
```

We have to consider the output stream we are using, specify exactly the operator being used, declare an instance of the Point class, and then return the output stream. This is a lot to consider. In Python, this code instead looks like this (assuming this is inside the Point class definition):

```
def __str__(self):
    return "(" + str(self.x) + "," + str(self.y) + ")"
```

The "__str__" magic method defines what it means for a Python object to become a string. Here we say that a Point becomes a string by printing the opening parenthesis, the integer x cast to a string, the comma, the integer y cast to a string, and the closing parenthesis. If I declare a Point instance `p` with values "(4,5)", we can do anything with it that we can do with other strings:

```
>>> print(p)
'(4,5)'
>>> message = "My point is " + str(p)
>>> print(message)
'My point is (4,5)'
>>> message = str(p) * 3
>>> print(message)
'(4,5)(4,5)(4,5)'
```

By defining one magic method our Point class has access to *everything strings can do in Python*. Nothing else needs to be defined.

A more useful example is the `__str__` magic method used in this project to print dictionaries, which in part looks like this:

```
printed_string = self.__class__.__name__ + ':\n'

    try:
        printed_string = printed_string + json.dumps(
            self.nGramCounts,
            sort_keys=True,
            indent=4,
            separators=(',', ': ')
        )
```

Here, we create a string that accesses the self.__class__.__name__ attribute, which is where Python automatically stores the name of the class. Then, we use the `json.dumps` function to turn all of `self.nGramCounts` into a string. The json library handles sorting our dictionary alphabetically and formatting it. The final method is a useful way to print the name and dictionary within any of our nGram models, which makes it much easier to debug and use our code.

Another common Python magic method is `__init__`, which is the constructor for an object. Our constructor for the nGramModel class just initializes the self.nGramCounts variable:

```
def __init__(self):
    self.nGramCounts = {}
```

Other common magic methods include `__eq__`, used to define when two objects are equal to each other, `__len__`, called when the `len` function is called to determine an object's length. 

