# Reach

[< back to specs](./)

Once you've finished the Core it's time to extend your learning model. The model you've built can generate new songs based on old song data. But it's limited. Its random data isn't always very good, and it still only has a terminal text interface. So for the Reach you will build on your learning model in three steps:

1) Pick an application for your model
2) Refine your model with heuristics until it produces good data
3) Showcase your model in some visually interesting or interactive way

By the end, you'll have the complete package, an interactive program that produces new works of art using modern techniques. Your final project will be your own unique Creative AI.

Note that you are welcome to use outside libraries and programs to make your final project as interesting as you desire. We do not require that you limit yourselves to the spec. However, when grading ***we will only download python libraries and not other external applications***. In addition, ***if you would like to substitute one component of the Reach with your own idea you must contact the staff first.***


# IMPORTANT

Any new python library you download to use for your REACH implementation **must** be added (and able to be installed) via setup.py in the main project directory. If we cannot install the library via setup.py alone, we cannot grade the portion of your REACH implementation which depends on that library.

# Table of Contents

- [Application](#application)
- [Heuristics](#heuristics)
- [Showmanship](#showmanship)
- [Getting New Data (optional)](#getting-new-data-optional)
- [Submission](#submission)

# Application

**What data is your model going to generate?** In the Core, we asked you to generate Beatles lyrics and Video Game Music. In the Reach, we'd like you to focus on one application. You may pick a different artist to imitate, another genre of music, etc. We suggest that you pick from one of the following categories:

#### Text
* Taylor Swift Lyrics
* Onion Headlines
* Poems
* Haikus
* Tweets

#### Music
* Video Game Music
* Guitar Music
* Classical Music
* Jazz
* Blues

**Requirements**
1. The data you generate needs to have some room to make errors. Tweets often have typos, Jazz is improvised, song lyrics are sometimes meaningless. Don't pick a highly precise Application.
2. You need to be able to collect enough data for your Application. You need a data set with thousands of tokens. For example, Taylor Swift has written dozens of songs, enough to train on thousands of tokens, but only a few dozen tweets, not enough data to train on. (An easy way to get around this is to propose a mashup by combining data from two different sources, such as combining Beatles and Taylor Swift lyrics.)

**Banned Reach Applications**

* Beatles Lyrics
* Donald Trump Tweets

# Heuristics

**How will you generate better data?** Once you've picked the data you're going to specialize in, you'll notice that it tends to follow some restrictions. Tweets, for example, have to fit within 280 characters. If you were generating tweets, you wouldn't want to just run the lyrics generator from the core and tweet the first 280 characters. You have to tweak your learning model with some set of heuristics to make it fit the data you're generating.

[Heuristics](./Concepts#heuristics) are simple rules which solve problems most of the time. Simple rules can be used to refine the output of your learning model. Most Artificial Intelligences, whether they play chess, trade stocks, or tag pictures don't only rely on a learning model. They incorporate little tricks and best practices that make the model seem smarter than it is. For instance, if you're racing a computer in Mario Kart, the AI drives slightly faster when you're ahead of it. The developers didn't program a better driver than you, they just tweaked the rules. These tweaks can seem arbitrary, with no rational basis, but they make your AI better.

Python has great libraries to help you refine your data. The two we will focus on are the ```pysynth``` and ```spacy``` libraries. You should have familiarity with ```pysynth``` from the core, which can be used to improve your music data. ```spacy``` is an [NLP](./Concepts#natural-language-processing) library for Python.

**Requirements**
1. You must use a new feature from `pysynth` if you are generating music or `spacy` if you are generating text. Several examples are listed at the end of this section.
2. You must use some other generic heuristics to improve the overall quality of your data. Pick some from the examples listed at the end of this section and justify why they are appropriate for your model.

Full points for a musical Reach requires that your song consist of at least two musical parts.

### Reuse sentences (general)

In the core, songs are generated with almost no repetition. Sentences are grouped together in the chorus and the two verses. But no sentence is ever repeated. Consider some real Beatles song lyrics:

```
It's been a hard day's night
And I've been working like a dog
It's been a hard day's night
I should be sleeping like a log
```

This chorus follows an ABCB pattern, where the first and third sentences are the same.

Music has this property too -- phrases or motifs are repeated throughout the length of the song. Consider one of the most famous pieces of music of all time, [Beethoven's Fifth Symphony](https://www.youtube.com/watch?v=_4IRMYuE1hI), whose repetition you will instantly recognize:

```DUN DUN DUN DUNNNNNNNNNN. DUN DUN DUN DUNNNNNNNNNN```

So when generating data, don't just randomly create 12 sentences and add them together. Lyrics repeat. Notes repeat. If you're composing a song, you may want some shorter element that repeats multiple times. The sentence patterns ABAB, ABCB, and ABCC are all very common.

Not all applications of your learning model will benefit. If you were generating haikus, it wouldn't make much to repeat whole phrases in such a short space.

### Build phrases (general)

Very closely related to the previous idea are repeated phrases. Your current models will always generate completely distinct sentences. But why should they? Turn again to the Beatles:

```
(Help!) I need somebody
(Help!) Not just anybody
(Help!) You know I need someone
(Help!)
```

Even though every sentence is different, they all start the same way -- the backup singers scream "Help!" Each sentence really has two parts. Consider another lyric example, where the phrase "love me do" is repeated multiple times:

```
Love, love me do
You know I love you
I'll always be true
So please, love me do
Whoa, love me do
```

The musical equivalent is a [motif](https://en.wikipedia.org/wiki/Motif_(music)), a short series of notes used throughout a piece. By repeating phrases within different parts of a song you can get more memorable pieces, songs with earworms or patterns you can hum to.

Play around with the `desiredLength` variable when you generate sentences and you can generate smaller parts which you then stitch together with larger ones.

### Filter your sentences (general)

With the random generation you have now, almost any sequence is possible. But not all sequences are possible in real data. Consider music again. Should it really be possible to follow any note with any other note? Perhaps we should require all the notes in a song to stay within the same key. 

We can do this via the `filter` parameter in `getNextToken`. Remember, you may modify any portion of the CORE project for your REACH implementation. You could create a `generateMusicalSentence` function which uses the `filter` parameter to constrain the possible tokens (notes) returned from `getNextToken`.



### Mix in pre-generated data (pysynth)

One way to improve your song data is to mix in background parts. This can make your songs more complicated and more pleasing to the ear without having to change the notes you're generating.

One way to harmonize your song is to mix it with [Pentatonic Scales](https://en.wikipedia.org/wiki/Pentatonic_scale). A Pentatonic Scale is a progression of notes on a scale of five notes per octave. For instance, the major pentatonic scale is comprised of the notes C, D, E, G, A. You might represent it in python like this:

```
>>> major_pentatonic_scale = [('c4', 4), ('d4', 4), ('e4', 4), ('g4', 4), ('a4', 4)]
```

Likewise, you might also choose to mix your song with a backbeat of one or more parts, which you might represent like this:

```
>>> backbeat = [('d1', 8), ('g1', 8)]
```

If your generated song is 120 notes, you would want to alternate between the notes of your backup part for the same length -- looping through your backbeat or scale progression until it is 120 notes long. Then you can mix it with your main song using pysynth's `mix_files` function.

### Using different instruments (pysynth)

Pysynth gives you the ability to choose different synthesizers. If you read through the pysynth code, you'll see several files named things like `pysynth_b.py` and `pysynth_e.py`. These files can each generate music much as pysynth in does in general, but will produce different sounds to fit different kinds of instruments. If you want to produce Jazz, the sounds you would want would be very different from if you were trying to create Guitar Music.

Consider which sounds you intend to use as it will make a big difference to your final product.

### Part of Speech Tagging (spacy)

To begin with SpaCy, first install it via pip as follows:

> $ pip install spacy


SpaCy requires creating "pipelines" or SpaCy objects. Pipelines are created by loading models, which are packages downloaded with SpaCy that provide information on specific parts of language -- vocabularies, syntaxes, translations, etc. Feel free to try out the model that you think will help your model most appropriately. 

The entire list of models can be found at https://spacy.io/models/ , but we'll just use the standard English model for this example. This can be installed by calling the following command in your terminal:

```
$ python -m spacy download en_core_web_sm 
```

Now we actually have to load that model into our program
```
>>> import spacy
>>> nlp = spacy.load("en_core_web_sm")
```
From here we can use our nlp object to decode specific parts of speech and analyze our sentences from there.

Let's say we want to analyze a string that says: 
> The apple does not fall far from the tree

We can do that by the following:

```
>>> doc = nlp("The apple does not fall far from the tree")
```

Now our doc variable holds a list of nlp objects, representing the tokens(words) in our original string, which we can decode with the following:

```
>>> for token in doc:
>>>     print token.text + " : " + token.pos_
```

This will iterate through every nlp object in the string and print it's text as well as it's part of speech, which will look something like this:

```
The : DET
Apple : NOUN
Does : VERB
Not : ADV
Fall : VERB
Far : ADV
From : ADP
The : DET
Tree : NOUN
```

Using this part of speech tagging, we can create a very powerful and effective set of rules for our text generation, turning our gibberish text into something that follows a set of rules that we can define. It's ultimately up to you how to make these rules and use them, but using the .pos_ member variable in SpaCy is a great start. 

Consider this fake onion headline:

> John Lennon Drags His Office Chair Everywhere He Goes And

The sentence almost makes sense -- if it had stopped at the word "Goes," it would have been perfect. Why should the sentence end on the word "And"? Right now the only relationship between words is that they match some ngram we saw in our trained data.

With spacy, we can determine individual parts of speech for a given a text, and decide whether or not our sentence is grammatically correct or complete according to how we want our sentences to be structured.

To fix this, we could write a rule saying that the last word of a generated headline can NOT be a conjunction, adjective, or determiner, which would give us the exact result that we want.

Additional documentation on POS tagging can be found at https://spacy.io/usage/linguistic-features

# Showmanship

**How will you display your model?** Your model may be doing very cool things, but it's still only a text-based menu interface that produces text or wav files. We want you to find some way to showcase your project, so that users can *see* the data you've produced. We suggest you pick one of the following applications (though you are free to pursue any different application of your choice, feel free to contact a staff member to discuss any reaches that interest you but aren't listed here):

### Twitterbot

Integrate your learning model with twitter. This reach will give you experience working with twitter's API and applying your model to other kinds of data. To begin, you'll need to download the python ```tweepy``` module. If you have pip installed you can install tweepy like this:

```pip install tweepy```

You will also need to [register a twitter account](https://twitter.com/signup/). Feel free to customize your account however you like, but **remember to keep it eecs183-appropriate.** You will need to [generate an access token](https://themepacific.com/how-to-generate-api-key-consumer-token-access-key-for-twitter-oauth/994/) (This is what will allow your project code to be authorized to use twitter's features.) Once you've done that, you can begin working with your twitter bot. A good explanation of how to get started can be found [here](http://pythoncentral.io/introduction-to-tweepy-twitter-for-python/).

Once you get your twitter bot working, you can extend it in whatever ways interest you. You could, for instance, train your bot on a public figure's timeline and generate new tweets for that figure. You could turn your twitter bot into a public interface for your music generation and attach songs as a wav file.

**Requirements**
1. You implement a bot which successfully reads from or posts to twitter when we run `generate.py`. Your bot does **not** need to run perpetually on a server to earn full points.
2. Your bot should run without our having to type in passwords. Your twitter bot should store its authentication keys in your project directory and read them at runtime. If we cannot test your bot we cannot grade it.

### Redditbot

Integrate your learning model with Reddit. This will give you real-world experience in using powerful API calls as well as understanding the potential for automated services in the many available public arenas. We recommend the python library **praw** (although Reddit itself has a very well documented REST API). To begin, you'll want to download the praw module:

```pip install praw```

You will also need to [create a reddit account](https://www.reddit.com/register/). This is your account once it is created, however **remember to keep it eecs183-appropriate**. You will need to [create an app key](https://www.reddit.com/prefs/apps/) (This will allow you to use the front-end API and submit POST requests to the Reddit server). [Following this guide may be a very helpful start](http://pythonforengineers.com/build-a-reddit-bot-part-1/).

Once you have your very own Reddit bot up and running there are many ways to extend it. Reddit itself has a variety of bots you'll see up and running while casually browsing the site which may give you inspiration. Your bot could post song links or upload word clouds about the post content. Find something that interests you and show us what is possible.

Please avoid spamming reddit -- your bot can be rate-limited by reddit or banned entirely if you spam too much in one subreddit. To help you out, we've created /r/eecs183, found [here](https://www.reddit.com/r/eecs183/). Please feel free to test and spam to your heart's desire here.

**Requirements**
1. You implement a bot which successfully reads from or posts to reddit when we run `generate.py`. Your bot does **not** need to run perpetually on a server to earn full points.
2. Your bot should run without our having to type in passwords. Your reddit bot should store its username and passwords in your project directory and read them at runtime. If we cannot test your bot we cannot grade it.

### Wordcloud

The [wordcloud library](http://amueller.github.io/word_cloud/) is used for creating [tag clouds](https://en.wikipedia.org/wiki/Tag_cloud) out of text data. This can be a powerful way to represent your musical or textual data, depending on what you decide to represent. Installation is minimal.

**Requirements**
1. Your program generate word clouds when we run the file `generate.py`.
2. Your program generate word clouds at runtime. It is not enough for you to submit word clouds you have produced, we must be able to generate them programmatically.

### Data Visualization

[matplotlob](http://matplotlib.org) and [plot.ly](https://plot.ly) are two graph-generating python modules you can use to represent your data. With graphing software you can focus on many aspects of your data -- you could, for instance, compare the most frequent words when you run your models on Beyonce lyrics vs. Taylor Swift lyrics, or you could create a picture of a song by plotting each note as a point on a graph.

**Requirements**
1. Your program generate graphs when we run the file `generate.py` which somehow relate to your model data.
2. Your program generate graphs at runtime. It is not enough for you to submit graphs you have produced, we must be able to generate them programmatically.

# Getting New Data (Optional)

## Lyrics
If your group chooses to use **lyrics** from an artist other than the Beatles, you can use the web scraper we have written to get the lyrics of the new artist and save them in the ```data/lyrics``` directory for you. A web scraper is a program that gets information from web pages: ours, which lives in the ```data/scrapers``` directory, scrapes the pages of [lyrics.wikia.com](http://lyrics.wikia.com/wiki/Lyrics_Wiki).

If you navigate to the ```data/scrapers``` folder and run the ```lyricsWikiaScraper.py``` file, you will be prompted to input the name of an artist. If that artist is found on lyrics.wikia.com, the program will make a folder in the ```data/lyrics``` directory for that artist, and save each of the artist's songs as a .txt file in that folder.

## Music
If your team chooses not to use the provided **music** from the Nintendo Gamecube, you will need to either use the ```vgMusicScraper.py``` file to get music data from another video game console, or else find an alternative way to get MIDI files.

To get new data for a video game console, run the ```vgMusicScraper.py``` program in the ```data/scrapers``` directory. The program will ask you to input the name of a platform; examples are "gameboy" or "xbox". To see the full list of platforms, take a look at the ```vgMusicPlatforms.txt``` file in the same directory - the platforms are the second column of data in that file. After you type in a valid platform, the program will grab MIDI files from [vgmusic.com](http://www.vgmusic.com) for that platform and call another program to convert those MIDI files into .txt files, saving all those files in the ```data/midi/<platform>``` directory. Don't be alarmed if this takes a little while, depending on the number of MIDI files it finds to download.

# Submission

We will grade the last submission to your GitHub team repository on the master branch before the project deadline. We will ***NOT*** grade earlier submissions, revert to an early commit, switch to a different branch, or make any changes to your project. We will run your project exactly as they are submitted. We will not grade changes pushed to your repository after the deadline.

Grading for the Reach is more open-ended than what you are used to from the rest of EECS 183. This is by design. The goal is for you to create something new that an autograder can't assign points to. This might make it hard to get a sense of when you're "done" with the Reach. While we can't grade your assignments ahead of time, successfully implementing the requirements for each Reach section is enough to earn full points.

**Requirements**
1. Your code must be pushed to your master branch on GitHub before midnight on the day of the deadline. You can verify your submission by navigating in your web browser to your repository page and examining the code files there.
2. You must include a file named `README.md` root directory of your repository. The `README.md` file must include a summary of what your reach does and instructions on how to run your program. Please copy the template from the [Grading](./Grading-Policy-and-Dates) section of the spec.
3. Everything must run from the main file `generate.py`. We will run all submissions by navigating to the project's root directory and running `python generate.py`.

**Notes:**

- You are allowed to change any of the functions we implemented for you: i.e. ```main```, ```getUserInput```, and so on. We've already autograded your core and there is no autograder for the reach.
- You are certainly allowed to play around with your music using software like Garage Band and the like. However, the only software we will consider when grading are python libraries which can be downloaded by the staff.
