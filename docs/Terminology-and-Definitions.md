# Terminology and Definitions

[< back to specs](./)

## Sections

- [Artificial Intelligence](#artificial-intelligence)
- [Natural Language Processing](#natural-language-processing)
- [Language Model](#language-model)
- [N-gram](#n-gram)
- [Training](#training)
- [Token](#token)
## Python: General Tutorials

In this project, you will be using Python3. To help you get started coding in Python, here are some links to short video tutorials. While most of this material will be covered in lecture, these videos can be used for reference if need be. They also emphasize features of Python that might be helpful for this project.

[Python Introduction](https://youtu.be/6XXH2tXTQ9g)

[Python While loops](https://youtu.be/Gd78bC5rsrk)

[Python Lists](https://youtu.be/VsZ6yqqbY0U)

[Python For loops](https://youtu.be/sdScQapHvXU)


## Artificial Intelligence

Artificial Intelligence is a branch of computer science concerned with programming computers to exhibit behavior they were not explicitly coded to do. For example, many people have been fascinated with having robots or simulations [learn to walk](https://youtu.be/yci5FuI1ovk?t=57), [play games] (https://www.youtube.com/watch?v=DlkMs4ZHHr8), or [hold conversations] (https://www.youtube.com/watch?v=WnzlbyTZsQY). In recent decades AI has given way to the more sophisticated <a href="http://openclassroom.stanford.edu/MainFolder/VideoPage.php?course=MachineLearning&video=01.2-Introduction-WhatIsMachineLearning&speed=100" target="_blank">machine learning</a>, which is the science of cleverly and efficiently structuring and training AI programs. Machine learning represents the modern form of AI because of its potential to work with unbelievably huge data to do anything from recommending your next Netflix binge to automatic, high-frequency stock trading.

<!--
Historically, AI began as a set of techniques for enumerating and searching through a series of possibilities. While this saw [historic success](https://www.youtube.com/watch?v=NJarxpYyoFI), most interesting problems have far too many, if not infinite possibilities to examine. Eventually search-based AI gave way to the more sophisticated machine learning, which is the science of cleverly and efficiently structuring and training AI programs. Machine learning represents the modern form of AI because of its potential to work with unbelievably huge data to do anything from recommending your next Netflix binge to automatic, high-frequency stock trading. Simply put, this project is an example of machine learning and machine learning is the future.
-->

## Natural Language Processing

Natural Language Processing is the area of computer science dedicated to understanding, working with, and generating human language. Some prominent modern examples include [Google search] (www.google.com), [Siri] (http://www.apple.com/ios/siri/), and the unquestioned Jeopardy champion, [Watson] (https://www.youtube.com/watch?v=WFR3lOm_xhE). Since this project involves handling and generating lyrics, it falls squarely in the domain of natural language processing.

## Language Model

A language model is a statistical model of a set of features in a language. For this project, we will model the transition probabilities between words. A transition probability is the probability of one event happening directly after another in a sequence of events. For example, taking words to be our events, if we see the word *yellow*, we want to estimate the probability that the next word is *submarine*; or if we see *strawberry fields*, we want to estimate the probability that the next word is *forever*. Different language models might instead learn the transition probabilities between different parts of speech, different semantic properties (e.g. active/passive sentences), or perhaps just different letters. They might also not use transition probabilities at all, but rather something different. 

## N-gram

An n-gram is a sequence of *n* words. A unigram is a single word (*imagine*), a bigram is a two-word sequence (*yellow submarine*), and a trigram is a three-word sequence (*in my life*). Practically speaking, natural language processing rarely considers anything larger than a fourgram, so we won't either.

Consider this sentence:

> *a rose is a rose is a rose*

There are 3 unique unigrams: *a*, *rose*, and *is*.
There are 3 unique bigrams: *a rose*, *rose is*, and *is a*.
There are 3 unique trigrams: *a rose is*, *rose is a*, and *is a rose*.

How about this one?

> *a rose is a flower is a rose*

This sentence contains 4 unigrams, 5 bigrams, and 6 trigrams. Can you identify them?

## Training

Training is the process by which most artificial intelligence programs learn from data. In our case, we use already-written lyrics to estimate the probability of one n-gram following another. For example, our model will be trained on data to learn how likely it is that *Eggman* follows *am the* versus how often *walrus* follows *am the*. 

## Token

A token is a single data point. For the core this means a word, with the only difference between a token and a word being that a word might have capitalization, punctuation, or other forms of noise. A token is a word after processing to make sure that semantically similar words like *ringo* and *Ringo* are reduced to the same basic word - likely *ringo*.

*Thanks to Reed Coke (former 183 GSI) for writing these.*
