# Concepts

[< back to specs](./)

The Creative AI Project contains a lot of code and concepts. This section explains the terms you are required to understand in order to complete the project.

## Table of Contents

- [Artificial Intelligence](#artificial-intelligence)
- [Heuristics](#heuristics)
- [Language Model](#language-model)
- [Natural Language Processing](#natural-language-processing)
- [N-gram](#n-gram)
- [Token](#token)
- [Training](#training)
- [PySynth](#pysynth)

## Artificial Intelligence

Artificial Intelligence is a branch of computer science concerned with programming computers to do things they were not explicitly coded to do. For example, AI can teach robots [how to walk](https://youtu.be/yci5FuI1ovk?t=57), [play games](https://www.youtube.com/watch?v=DlkMs4ZHHr8), or [hold conversations](https://www.youtube.com/watch?v=WnzlbyTZsQY).

Historically, AI began as a set of techniques for enumerating and searching through a series of possibilities. For example, this is how the [Deep Blue supercomputer beat world chess champion Garry Kasparov](https://www.youtube.com/watch?v=NJarxpYyoFI). Deep Blue used rules and heuristics to consider thousand of possible chess moves before picking the best one. However, most interesting problems have far too many (if not infinite) possibilities to examine. 

In recent decades AI has focused on more sophisticated [Machine Learning](http://openclassroom.stanford.edu/MainFolder/VideoPage.php?course=MachineLearning&video=01.2-Introduction-WhatIsMachineLearning&speed=100) techniques. ```Machine Learning``` is the science of training AI programs to teach themselves how to solve problems. A Machine Learning chess AI would examine thousands of chess games and try to understand what makes some moves better than others. It would then use the lessons it had learned to make the best moves.

Machine Learning represents the modern form of AI. This is the kind of AI you will build in this project.

## Heuristics

```Heuristics``` are rules for solving problems that give "good-enough" answers. They aren't perfect but can be easy to work with. For example, "if you see clouds in the morning, carry an umbrella" is a heuristic which is easier than calculating a weather forecast, though it might not work as often. Heuristics are commonly used in Artificial Intelligence to improve performance. One of the heuristics you will use in the Core is that notes in a song should all be in the same key. For the Reach we will ask you to develop your own heuristics to improve the quality of your data.

## Language Model

A ```language model``` is a statistical model of a set of features in a language. Our language model will model the transition probabilities between words and notes. A transition probability is the probability of one event happening directly after another in a sequence of events. For example, taking words to be our events, if we see the word *yellow*, we want to estimate the probability that the next word is *submarine*; or if we see *strawberry fields*, we want to estimate the probability that the next word is *forever*. Different language models might instead learn the transition probabilities between different parts of speech, between different letters, or something completely different. 

## Natural Language Processing

Natural Language Processing is the area of computer science dedicated to understanding, working with, and generating human language. Some prominent modern examples include [Google search](www.google.com), [Siri](http://www.apple.com/ios/siri/), and the Jeopardy champion, [Watson](https://www.youtube.com/watch?v=WFR3lOm_xhE). Since this project involves handling and generating lyrics, it falls squarely in the domain of natural language processing.

## N-gram

An ```n-gram``` is a sequence of *n* words. A unigram is a single word (*imagine*), a bigram is a two-word sequence (*yellow submarine*), and a trigram is a three-word sequence (*in my life*). Practically speaking, natural language processing rarely considers anything larger than a fourgram, so we won't either.

Consider this sentence:

> *a rose is a rose is a rose*

There are 3 unique unigrams: *a*, *rose*, and *is*.
There are 3 unique bigrams: *a rose*, *rose is*, and *is a*.
There are 3 unique trigrams: *a rose is*, *rose is a*, and *is a rose*.

How about this one?

> *a rose is a flower is a rose*

This sentence contains 4 unigrams, 5 bigrams, and 6 trigrams. Can you identify them?

## Training

Training is the process by which most artificial intelligence programs learn from data. In our case, we will train on Beatles lyrics and Gamecube Music.  to estimate the probability of one n-gram following another. For example, our model will be trained on data to learn how likely it is that *Eggman* follows *am the* versus how often *walrus* follows *am the*. 

## Token

A token is a single data point. For our lyrics generation this means a word, except that a token has no capitalization, punctuation, or other noise. Before training our language models we process them into tokens so that semantically similar words like *ringo* and *Ringo* are reduced to the same basic word *ringo*. For our music generation each token is a note.


## PySynth

**[PySynth](https://mdoege.github.io/PySynth/)** is a Python module that synthesizes music. It takes music notes in the form of a list of tuples, and outputs those notes to a ```.wav``` file.

In PySynth, a note is represented as a *(string, integer)* tuple. The first item in the tuple is the pitch of the note, which tells you the "high" or "low" the note will be. The second item in the tuple is the duration of the note, which tells you how long the note will last. 

You will need to parse and/or create PySynth tuples to generate music with your learning models. Therefore, let's take a look at some example PySynth tuples to get a feel for how they work:

```
>>> c = ('c4', 2)
>>> fSharp = ('f#6', 1)
>>> aFlat = ('ab3', 16)
>>> rest = ('r', 4)
```

- The first tuple, ```c```, is a note with a pitch of "c4". The 4 in "c4" gives us information about the note's *octave* value: in other words, it represents how high this note is relative to other notes. "c5" would be higher than "c4" and "c3" would be lower than "c4". This note has a duration of 2, relatively longer than most other notes. (Duration values closer to 0 belong to longer notes.)
- The second tuple, ```fSharp```, is a note with a pitch of "f#6". The "#" in "f#6" is a musical symbol which means that this pitch is sharp, higher in pitch than a regular "f". Note that "f#" and "f" are different notes. Its duration is 1, which means that this note is the longest note that PySynth can play.
- The third tuple, ```aFlat```, is a note with a pitch of "ab3". The "b" in "ab3" is a "flat", which is a musical symbol that means that this pitch is lower in pitch than a regular "a". Its duration is 16, which means that this note is rather short.
- The final tuple, ```rest```, is a musical "pause" - the 'r' means a silence. Its duration is 4, which is equivalent to one quarter note.

To actually generate a .wav file using PySynth, you call ```pysynth.make_wav(tuplesList, fn=songName)```. The first parameter, ```tuplesList```, is a list of PySynth tuples that represents a song. The second parameter tells PySynth what to name the output .wav file. Here is an example program that uses PySynth to output a song named test.wav:

```python
import pysynth
mySong = [ ('e4', 4), ('d4', 4), ('c4', 4) ]
pysynth.make_wav(mySong, fn='test.wav')
```

Don't forget to specify the `fn=` in the second parameter -- the output file name is a ```named parameter```.
