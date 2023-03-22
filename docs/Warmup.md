# Warmup

[< back to specs](./)

## Table of Contents

- [General](#general)
- [New Concepts](#new-concepts)
  - [Doctests](#doctests)
  - [Imports](#imports)
  - [Pass](#pass)
  - [In Operator](#in-operator)
  - [Foreach Loops](#foreach-loops)
  - [Dictionaries](#dictionaries)
  - [Tuples](#tuples)
  - [Classes](#classes)

## General

The Warmup consists of practice functions to teach you the Python constructs you will use for the rest of the project. It is entirely contained in the file ```warmup.py``` in the ```warmup``` folder. Each function has a set of public test cases; we will use these same test cases to grade your submission. We will only grade one submission, the ```warmup.py``` contained in your ```warmup``` folder when you submit the project. However, even though we will only grade submission, ***it is expected that every team member completes and understands the Warmup. If you do not understand the Warmup you will not understand the rest of the project.***

Also note that the Warmup ***will*** be graded along with your core, so a working solution must be pushed to your GitHub Repository.

To run the Warmup, open python on ```warmup.py```, or use terminal to step into the ```warmup``` directory and run:

```python warmup.py```

An error message should print specifying that you are failing most of the test functions. When you have finished the warmup, running the file should produce no output.

## New Concepts

### Doctests

Python allows test cases to be built directly into a function's documentation. ```doctests``` are the first comments right after the line where a function is defined. Every line in the comment preceded with ```>>>``` is part of the test case to be run; every line without the ```>>>``` is the expected result. For example:

```
def add(a, b):
  """This function returns the sum of a and b.
  >>> add(2, 3)
  5
  >>> add(0, -1)
  -1
  >>> x = 5
  >>> y = 4
  >>> add(x, y)
  9
  """
  return a + b
```

Inside ```main()``` we only need to import the doctest module and run it:

```
import doctest
doctest.testmod()
```

The ```doctest``` module will then see the test cases in ```add()``` and run them. If ```add(2, 3)``` does not evaluate to ```5```, doctest will report an error.

We will grade your Warmups out of how many function doctests your submission passes. We will not run any other test cases.

### Imports

```import``` is how we include ```modules``` in our files. The idea is the same as ```#include``` in C++ -- add libraries of code we want to use to our project. For example, to be able to run doctests, we import the doctests module by saying:

```import doctest```

### Pass

```pass``` is a Python keyword that means "do nothing". All the functions in the Warmup are stubbed out by only having the line ```pass``` as their implementation. You should remove this line as you implement your functions.

### ```in``` Operator

```in``` is a Python operator that returns ```True``` or ```False``` on whether a value is inside some container. Consider the following example:

```
>>> beatles = ["john", "paul", "george", "ringo"]
>>> "john" in beatles
True
>>> "mary" in beatles
False
```

This is a very powerful operator because it allows us to quickly check membership in a container. Consider the equivalent C++ code:

```
int beatles[4] = {"john", "paul", "george", "ringo"};
for(int i = 0; i < 4; ++i) {
    if (beatles[i] == "john") {
        return true;
    }
}
return false;
```

The ```in``` operator is even more powerful because it also works with dictionaries and tuples:

```
>>> wordcounts = { "hard" : 1, "day": 1, "night" : 1}
>>> "hard" in wordcounts
True
>>> note = ("c4", 16)
>>> "c4" in note
True
```

Understanding the ```in``` operator will allow you to write much simpler code on the project.

### Foreach Loops

Python allows you to iterate through a list without using an index. Fox example:

```
>>> beatles = ["john", "paul", "george", "ringo"]
>>> for member in beatles:
...   print("* " + member)
...
* john
* paul
* george
* ringo
```

Here, when we say `for member in beatles`, `member` iterates through every value in the `beatles` list. Here, we print that `member` with a bullet point to make a list. This is much simpler than the C++ equivalent, where we have to declare an index iterating through `0` to `size - 1` and use that to index into the list. If we wanted to use that ```range-based``` syntax in Python it would look like this:

```
>>> beatles = ["john", "paul", "george", "ringo"]
>>> for i in range(len(beatles)):
...   print("* " + beatles[i])
...
* john
* paul
* george
* ringo
```

Just like with the `in` operator, we can also use `foreach` loops to iterate through dictionaries and tuples:

```
>>> wordcounts = { "hard" : 1, "day": 1, "night" : 1}
>>> for word in wordcounts:
...   print(word)
...
"hard"
"day"
"night"
>>> note = ("c4", 16)
>>> for part in note:
...   print(part)
...
"c4"
16
>>>
```

Knowing how to use a `foreach` loop is an important part of understanding and coding in Python.

### Dictionaries

```dictionaries``` are objects which **map** one value to another value. Dictionaries are like arrays, except that the index, called a ```key```, can be any value, not only a number between 0 and the array size. Take these python terminal commands as an example:

```
>>> myDict = {}
>>> myDict
{}
>>> myDict[0] = 5
>>> myDict
{0: 5}
>>> myDict["Hey"] = "Jude"
>>> myDict
{0: 5, 'Hey': 'Jude'}
>>> myDict[0]
5
>>> myDict["Hey"]
'Jude'
```

Here we can create the key-value pairs of ```0: 5``` and ```'Hey': 'Jude'```. We can then say ```myDict["Hey"]```, which evaluates to ```'Jude'```.

You can even have a dictionary inside a dictionary:

```
>>> inner = {}
>>> outer = {}
>>> inner["Me"] = "Do"
>>> outer["Love"] = inner
>>> outer
{'Love': {'Me': 'Do'}}
```

Dictionaries are at the core of the Creative AI learning models.

### Tuples

Python ```tuples``` are **immutable** sequences of objects. Like Python lists, they can contain objects of different types, can be indexed using square brackets starting at 0, and can be sliced. However, they cannot be changed after creation. Also, they are written using parentheses instead of square brackets.

Here are some examples:

```python
>>> beatlesTuple = ('all', 'you', 'need', 'is', 'love')
>>> nestedTuple = (1, (2, (3, 4)))
>>> multiTypeTuple = (3.14, 'pi')
```

Because tuples are immutable, you **cannot** do things like:

```
>>> multiTypeTuple = (3.14, 'pi')
>>> multiTypeTuple[0] = 3.14159
TypeError: 'tuple' object does not support item assignment
```

If you *really* wanted to update a tuple, you could make a new tuple out of existing tuples:

```python
>>> song1 = ('hey', 'jude')
>>> song2 = ('dont', 'make', 'it', 'bad')
>>> song3 = song1 + song2
>>> song3
('hey', 'jude', 'dont', 'make', 'it', 'bad')
```

Tuples are very important for generating music -- they're how the ```pysynth``` library represents notes.

### Classes

Classes do the same thing in Python that they do in C++, but there are a lot of differences. Take a look at the syntax in this example class and note the differences:

```python
class Album:

    # Albums all have song lyrics
    def printLyrics(self):
        lyrics = "Here Comes the Sun"
        print lyrics

    # Albums sell
    def sales(self):
        self.copies_sold = 20;
    
    # Some songs have co-writers who get a cut
    def payCoWriters(self):
        return 100000
```

* To instantiate an ```Album``` object, you could do something like the following: 

```
>>> a = Album()
```

* There's no concept of public or private with Python classes. Everything is accessible to the public, which eliminates the needs for getters or setters. To access class member attributes, you use the dot operator, as in C++. For example:

```
>>> a.sales()
>>> a.copies_sold
20
```

* The keyword ```self``` in Python means “this instance of the class”. You only use it inside the definition of the class. ```self``` is the first parameter of class functions, and class member variables always start with ```self``` followed by the dot operator. For example, in the class above, ```copies_sold``` is a member variable of the ```Album``` class, but ```lyrics``` is not:

```
>>> a.lyrics
AttributeError: Album instance has no attribute 'lyrics'
```

* While ```self``` gets passed as a parameter in the definitions of member functions, you don't need to use it when calling those functions. For example:

```
>>> a.payCoWriters()
20000
```
