# Python 3

[< back to specs](./)

To this point in EECS 183 you've used Python 2, but for this project we'll want to use Python 3. Python 3 is the most current version of the language, and as of now the majority of packages are being built on this version. This is mainly because Python 2 is no longer going to be supported past 2020; (you can keep track here: https://pythonclock.org/ )

To install Python 3 you should follow the tutorial relevant to your system.
# Windows
While to this point the shell that you're most familiar with in Windows 10 may be Git Bash, for this project we recommend using "Powershell", a built in program to windows 10.

### Installing the Package Manager Chocolatey
Chocolatey is a package manager built for windows that works exactly like apt-get in Linux/Mac. Chocolatey will help us quickly install applications and tools directly into our shell, and we will be using it to download both Python3 and the packages we need for our project.

To install Chocolatey, we need to open CommandLine in administrative mode. `Windows+R` will open the run prompt. Then type `cmd` and then `ctr+shift+enter`. CommandLine should now be open in administrative mode.

With CommandLine open, copy+paste the following:

```
@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
```

If we need to upgrade Chocolatey at any point in the future we can use:

```$ choco upgrade chocolatey```

With our package manager installed, we can now install Python 3 directly. 

Following this install, we may use either `CommandLine` or `PowerShell`. Personally, I am usering `PowerShell`. Make sure when using either, you are in administrative mode.

### Installing Python 3

We can now use Chocolatey to install Python 3 like this:

```$ choco install python3```

Once the process is completed, you should see the following output:
```
Environment Vars (like PATH) have changed. Close/reopen your shell to
 See the changes (or in powershell/cmd.exe just type 'refreshenv').
The install of python3 was successful.
 Software installed as 'EXE', install location is likely default.

Chocolatey installed 1/1 packages. 0 packages failed.
 See the log for details (C:\ProgramData\chocolatey\logs\chocolatey.log).
 ```

With the installation finished, you'll want to confirm that Python is installed and ready to go. Restart powershell by closing it and reopening as Administrator. Now check the version of python that you have installed:

```$ python -V```

which should print: ```Python 3.X.X```. If you have a different version (i.e. <= 3), check either on Piazza or ask a member of staff to help you install Python3.

And just like that you have Python 3 on your computer! Pat yourself on the back, you can now start Creative-AI!

# Mac

For Mac users, we will ask that you use `Brew` as your package manager. To install `brew`, open up `Terminal` and copy-paste the following:

``` bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Once this process has finished, copy-paste the following:

``` bash
echo 'export PATH=/usr/local/bin:/usr/local/sbin:$PATH' >> ~/.bash_profile
```

This command tells your computer to look at `Brew` install directories first before anywhere else. This can help ensure that you are using the correct installations.

Now we can install python, type the following in `Terminal`:

``` bash
brew install python
```

You should now be able to run `python3` as a command in `Terminal`. Go ahead and try it out, it should look like this (Your version may be different, as long as it is >= 3.6.4):

``` bash
heads/master⇥ python3
Python 3.6.4 (default, Mar  9 2018, 23:15:12) 
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.39.2)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

To exit this screen you may type: `ctr+D`

# Using Python 3

For your project, you will be required to create a virtual environment.

For the rest of the tutorial I will be using `python3` to mean 'Running Python 3'

***Windows users will be using the command `python` instead of `python3` unless specified otherwise.***

Open up `Powershell` or `Terminal` in your project directory and run the following:

```
python3 -m venv env
```

This will create a virtual environment in the current working directory.

Next, enter the virtual environment.

#### Windows:

PowerShell:
``` PowerShell
env\Scripts\activate
```

#### Mac:

``` bash
source env/bin/activate
```

### **Important**

***You must always enter the virtual environment before running any code in this project. The remainder of the tutorial will assume that you are inside the virtual environment.***

# Installing Project Files

Before you can run the main (`generate.py`) program, you will need to install the `creative_ai` project.

First, update pip using `pip install --upgrade pip` as the version installed by default is not up to date.

In the main directory (where the `creative_ai` folder and `setup.py` is) run the following command:

`pip install -e .`

This will install all of the dependencies listed in `setup.py`. Whenever you add a new dependency to your project, i.e. `spacy, praw` it **must** be installed from the `setup.py` file.


Now the project should be able to run. To test this, run (in `PowerShell / Terminal`), navigate to the creative_ai folder and run:

`python generate.py`

from within the `creative_ai` folder. This will run the main program your project is based off of.


