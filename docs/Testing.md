# Testing

[< back to specs](./)

Testing in Python is very different from testing in C++. We still expect that everybody is comfortable testing and running their code in order to check for correctness. This page is for strategies to help you test your code as you complete the project.

# Why is testing in Python different?

Python code isn't compiled. C++ is a compiled language where code is transformed by the compiler from C++ into binary code. This means that lots of errors can be detected before the program has run. Python is an interpreted language where code is turned into binary line by line as it is interpreted. This means that a lot of errors can only be caught by Python in runtime. Since we don't have Visual Studio or XCode to step through compiled Python code, we need to find other ways to test.

# Using `print` Effectively

Without an IDE that lets you step into and out of your test cases, one of the best ways to debug is to print output. Let's say you have a bug in your sentence generation. Is it because of the way you generate sentences, or are your models wrong? You might think that your models work correctly, but what happens if you give them an example sentence to train on and then print the model? Do they have the value you expected them to have? This is exactly what one of the test cases we gave you in `unigramModel.py` does:

```
uni = UnigramModel()
text = [ [ 'brown' ] ]
uni.trainModel(text)
# Should print: { 'brown' : 1 }
print(uni)
```

If your model is correct, you might go back to looking at your sentence generation. If your output isn't correct, you know that you have an error coming from your `trainModel` function. You might then consider printing variables in your `trainModel` function to further isolate the problem.

Just remember that if you add print statements inside a function you will want to take them out before you submit your final code.

# Testing Modules Individually

At the bottom of every file that you will edit for this project, you will find this line:

```
if __name__ == '__main__':
```

This conditional returns true when a file is run as the main file of a project. You can use this to run different code when you run a module as main as opposed to when you import from it. (Unlike C++, you can have multiple mains throughout your project with test cases in each -- Python will only run one file as main.) This offers a really straightforward way to test individual python files without testing your entire project.

You should start by developing some test cases for each file. We've given you example test cases in the `unigramModel.py` file, which will only run when you run the file as main. Right now there are test cases that test the `trainModel` and `trainingDataHasNGram` functions. Each of them creates a `unigramModel` and trains it on a small sample text. The output of the test case should be small enough that you can read the whole dictionary it prints and see if you're getting the correct output. You will want to consider how you should test the `getCandidateDictionary` function, and then write similar test cases for the `bigramModel` and `trigramModel` classes.

# Reading Errors

When Python crashes, it generally gives you a lot of information. Consider an (incorrect) example Python file:

```
def foo(x):
    myDict = {}
    return myDict[x]

def bar(x):
    return x + 1

if __name__ == "__main__":
    print(bar(5))
    print(foo(5))

```

This is syntactically valid Python, so Python will attempt to run the file, but will produce this as output:

```
Traceback (most recent call last):
  File "example.py", line 10, in <module>
    print(foo(5))
  File "example.py", line 3, in foo
    return myDict[x]
KeyError: 5
```

Let's break it down.

The first line announces the "Traceback". A traceback is a list of functions that caused the crash.

The lines after that are the traceback itself. The first line in the traceback is where the program started and the last line is where the program crashed. Everything in between is the path Python traveled from the start of the program to the crash.

Here, we see that we started in `<module>`, and called `print(foo(5))`. Then inside `foo` we reached the line `return myDict[x]`, which caused the crash. So we can tell that calling `bar` did not cause the program to crash, and that our problem happens inside `foo` when we access `myDict[x]`.

The last line in the traceback is the error Python returned. Python tries to give a name for every error that causes a crash. Here, we see that a `KeyError` was thrown, and it also prints the value `5`.

A `KeyError` happens whenever Python tries accessing a dictionary with some key which does not exist in that dictionary. Here, we access `myDict` with value `5`, but `5` does not exist in that dictionary, so we get a `KeyError` and Python crashes. To fix the problem we would have to remove the bad dictionary access or put the value `5` in our dictionary.

Now that you know how to read a Python error, here are the most common errors you will encounter:

* `KeyError`: Caused when a dictionary is indexed by some value it doesn't contain
* `IndexError`: Caused when a list index goes out of bounds. (C++ did not stop these errors.)
* `NameError`: Caused when you use some variable that does not exist in your current scope
* `IndentationError`: Your Python file is not indented correctly
* `TypeError`: Caused by using the wrong type of object (i.e., if you said `"hello world" / 2`)
* `SyntaxError`: Caused when your Python is not syntactically correct (similar to a compile error in C++)

