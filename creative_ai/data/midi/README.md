# Converting midi data to pysynth

If you choose to download more midi data for your Reach, you'll need to convert it into a format pysynth can understand. Everything you need has already been provided for you. It will take two conversions, from midi to ascii, and from ascii to pysynth's format.

## Converting midi to ascii

The `mid2asc.c` file in this folder can convert midi files into ascii text. (Credit to A.P.Shelby for writing this open-source code and the [documentation here](http://www.archduke.org/midi/instrux.html).)

Compile the file in Visual Studio or Xcode. Although it is C code, not C++, you should be able to compile it just like the other C++ code you've compiled in this course. You should put the executable into this folder.

When you've successfully compiled it, you can convert one file by stepping into the directory where the `mid2asc` executable lives and with a terminal command as such:

`./mid2asc midifile > textfile`

This will convert the file named `midifile` into a file containing the ascii text named `textfile.`

## Converting ascii to pysynth

This step has already been completed for you. If you read the `dataLoader.py` file in the `data/` folder, you'll see that the function `loadMusic()` calls the function `formatPitch()`, which is our code to convert from ascii text to something pysynth will understand. All that means is that in your python code you will need to call the `loadMusic()` function as such:

`>>> musicalText = loadMusic("MUSIC DIRECTORY")`

For example, if you downloaded gameboy music and put it in a folder named `gameboy`, you would code this:

`>>> musicalText = loadMusic("gameboy")`

The `loadMusic()` function will return text structured exactly as you worked with it in the core, lists of musical notes where the first elements in the list are the starting tokens `^::^` and `^:::^` and the last element in the list is the ending token `$:::$`.
