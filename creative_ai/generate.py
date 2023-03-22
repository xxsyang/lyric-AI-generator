#!/usr/bin/env python
import sys
sys.dont_write_bytecode = True # Suppress .pyc files

import random
import numpy as np
from PIL import Image
import pysynth
from creative_ai.utils.menu import Menu
from creative_ai.data.dataLoader import *
from creative_ai.models.musicInfo import *
from creative_ai.models.languageModel import LanguageModel
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import spacy
# FIXME Add your team name
TEAM = 'IHXJ'
LYRICSDIRS = ['Taylor_swift']
TESTLYRICSDIRS = ['the_beatles_test']
MUSICDIRS = ['gamecube']
WAVDIR = 'wav/'

def output_models(val, output_fn = None):
    """
    Requires: nothing
    Modifies: nothing
    Effects:  outputs the dictionary val to the given filename. Used
              in Test mode.

    This function has been done for you.
    """
    from pprint import pprint
    if output_fn == None:
        print("No Filename Given")
        return
    with open('TEST_OUTPUT/' + output_fn, 'wt') as out:
        pprint(val, stream=out)

def sentenceTooLong(desiredLength, currentLength):
    """
    Requires: nothing
    Modifies: nothing
    Effects:  returns a bool indicating whether or not this sentence should
              be ended based on its length.

    This function has been done for you.
    """
    STDEV = 1
    val = random.gauss(currentLength, STDEV)
    return val > desiredLength

def remove_special_POS(ll):
    """
    # The end of a sentence cannot be a conjunction, adjective or determiner
    """
    # load training model
    nlp = spacy.load('en_core_web_sm')
    # init a temp list 
    R = []
    # loop for the input list
    for l in ll:
        # get the last one word
        doc = nlp(l[-1])
        # if the last one word is conjunction or adjective or determiner
        if doc[0].pos_ in ['CONJ','ADJ','DET']:
            # delete this word
            l.pop()
        # result list add the deleted list o
        R.append(l)
    # return result
    return R

def get_new_list(ll):
    """
    # Use desiredlength to judge whether the sentence is too long. 
    # When the sentence is too long, cut it, and sew the smaller part 
    # and the larger part together
    """
    #Initializing a result list 
    result = []
     # Initializing a temp list
    r1 = []
    # set desiredLength
    desiredLength = 5
    # lucky = random.randint(0,len(r1)-1)
    # if r1[lucky] != i:
    #     r1[lucky].extend(i)
    #Loop through the entered list
    for l in ll:
        # Call the sentencetoolong function to determine whether the 
        # sentence length is too long
        if sentenceTooLong(desiredLength,len(l)):
            # Cut sentences when they are too long
            r1.append(l[:desiredLength])
    # Loop through the cropped results
    for i in r1:
        # Discard a sentence when its length equals desiredlength
        if len(i) == desiredLength:
            # skip 
            continue
    result = r1
    #print(result,ll)
    return result


def printSongLyrics(verseOne, verseTwo, verseThree, chorus):
    """
    Requires: verseOne, verseTwo, and chorus are lists of lists of strings
    Modifies: nothing
    Effects:  prints the song.
    
    This function is done for you.
    """
    # to achieve sentence cutting 
    verseOne = get_new_list(verseOne)
    verseTwo = get_new_list(verseTwo)
    Chorus = get_new_list(chorus)

    # remove conjunction, adjective or determiner at the end of a sentence
    verseOne = remove_special_POS(verseTwo)
    verseTwo = remove_special_POS(verseTwo)
    chorus = remove_special_POS(chorus)

    # Obtain a random number and generate different templates based on the random number
    lucky = random.randint(0,3)
    if lucky == 0 :
        # acbc
        verses = [verseOne, chorus, verseTwo, chorus]
    elif lucky == 1:
        # abcb
        verses = [verseOne, verseTwo,chorus, verseTwo]
    elif lucky == 2:
        # abcc
        verses = [verseOne,verseTwo, chorus,chorus]

    verses = [verseOne, chorus, verseTwo, chorus]
    # init a list
    word = []
    print()
    # Loop through verses
    for verse in verses:
        # Loop through verse
        for line in verse:
            # print the Lyric
            print((' '.join(line)).capitalize())
            # get temp list of all Lyric
            temp = (' '.join(line)).capitalize()
            # get all Lyric
            word.extend(temp.split(' '))
        print()
    # trun list to string
    word = ' '.join(word)
    # get the mask picture of wordcloud
    mask = np.array(Image.open('girl.png'))

    wc = WordCloud(
               # backgroud color
               background_color = "white",
               # the maximum number of the words
               max_words= 1000, 
               # the maximum size of the word
               max_font_size = 500,
               # the minimum size of the word
               min_font_size = 20, 
               # roomdom number
               random_state = 42, 
               # prevent the same words appear
               collocations = False,
               # shade the image
               mask = mask,
               # plt.figure(dpi=xx)
               width = 1600,height = 1200,margin = 10,
               )
    wc.generate(word)
    # zoom in and zoom out
    plt.figure(dpi = 100) 
    plt.imshow(wc, interpolation = 'catrom',vmax = 1000)
    # hinding the axis
    plt.axis("off") 
    wc.to_file('wordcloud.png')
    print('wordcloud has saved')
    
def trainLyricModels(lyricDirs, test=False):
    """
    Requires: lyricDirs is a list of directories in data/lyrics/
    Modifies: nothing
    Effects:  loads data from the folders in the lyricDirs list,
              using the pre-written DataLoader class, then creates an
              instance of each of the NGramModel child classes and trains
              them using the text loaded from the data loader. The list
              should be in tri-, then bi-, then unigramModel order.
              Returns the list of trained models.
              
    This function is done for you.
    """
    model = LanguageModel()

    for ldir in lyricDirs:
        lyrics = prepData(loadLyrics(ldir))
        model.updateTrainedData(lyrics)

    return model

def trainMusicModels(musicDirs):
    """
    Requires: musicDirs is a list of directories in data/midi/
    Modifies: nothing
    Effects:  works exactly as trainLyricsModels, except that
              now the dataLoader calls the DataLoader's loadMusic() function
              and takes a music directory name instead of an artist name.
              Returns a list of trained models in order of tri-, then bi-, then
              unigramModel objects.
              
    This function is done for you.
    """
    model = LanguageModel()

    for mdir in musicDirs:
        music = prepData(loadMusic(mdir))
        model.updateTrainedData(music)

    return model

def runLyricsGenerator(models):
    """
    Requires: models is a list of a trained nGramModel child class objects
    Modifies: nothing
    Effects:  generates a verse one, a verse two, and a chorus, then
              calls printSongLyrics to print the song out.
    """
    verseOne = []
    verseTwo = []
    verseThree = []
    chorus = []

    for _ in range(4):
        verseOne.append(generateTokenSentence(models, 7))
        verseTwo.append(generateTokenSentence(models, 7))
        verseThree.append(generateTokenSentence(models,7))
        chorus.append(generateTokenSentence(models, 9))

    printSongLyrics(verseOne, verseTwo, verseThree, chorus)

def runMusicGenerator(models, songName):
    """
    Requires: models is a list of trained models
    Modifies: nothing
    Effects:  uses models to generate a song and write it to the file
              named songName.wav
    """

    verseOne = []
    verseTwo = []
    chorus = []

    for i in range(4):
        verseOne.extend(generateTokenSentence(models, 7))
        verseTwo.extend(generateTokenSentence(models, 7))
        chorus.extend(generateTokenSentence(models, 9))

    song = []
    song.extend(verseOne)
    song.extend(verseTwo)
    song.extend(chorus)
    song.extend(verseOne)
    song.extend(chorus)
    
    print(song)
    pysynth.make_wav(song, fn=songName)

###############################################################################
# Begin Core >> FOR CORE IMPLEMENTION, DO NOT EDIT OUTSIDE OF THIS SECTION <<
###############################################################################

def generateTokenSentence(model, desiredLength):
    """
    Requires: model is a single trained languageModel object.
              desiredLength is the desired length of the sentence.
    Modifies: nothing
    Effects:  returns a list of strings where each string is a word in the
              generated sentence. The returned list should NOT include
              any of the special starting or ending symbols.

              For more details about generating a sentence using the
              NGramModels, see the spec.
    """
    # Generate a sentence
    # Initial sentence with starting token
    word_list = ['^::^', '^:::^']
    # get token one by one
    while True:
        # get next token with current sentence
        candidate_word = model.getNextToken(word_list)
        # if next token is ending token, end the sentence
        if candidate_word == '$:::$':
            break
        # append next word to the current
        word_list.append(candidate_word)
        # if sentence length is too long , end the sentence
        if sentenceTooLong(desiredLength, len(word_list) - 2):
            break
        if desiredLength <= len(word_list) - 2:
            break
    # remove the starting token from sentences
    word_list.pop(0)
    word_list.pop(0)
    ret_list = []
    # loop the sentence, difference operations between with music and lyrics
    for value in word_list:
        if '(' in value:
            # Always music come to this situation
            # change string value "('c4', 16)" to list ['c4', 16]
            # remove '(' and ')'
            value = value.replace('(', '')
            value = value.replace(')', '')
            # divided string value into two part,
            tmp_list = value.split(',')
            # remove space value and '''
            key1 = tmp_list[0].strip().strip('\'').strip()
            val1 = tmp_list[1].strip()
            # generate a new list
            tmp_list2 = []
            tmp_list2.append(key1)
            tmp_list2.append(int(val1))
            # music situation return a list of lists
            ret_list.append(tmp_list2)
        else:
            # lyrisc situation return a list of string
            ret_list.append(value)
    return ret_list

###############################################################################
# End Core
###############################################################################

###############################################################################
# Main
###############################################################################

PROMPT = [
    'Generate song lyrics by Taylor_swift',
    'Generate a song using data from Nintendo Gamecube',
    'Quit the music generator'
]

def main():
    """
    Requires: Nothing
    Modifies: Nothing
    Effects:  This is your main function, which is done for you. It runs the
              entire generator program for both the reach and the core.

              It prompts the user to choose to generate either lyrics or music.
    """

    mainMenu = Menu(PROMPT)

    lyricsTrained = False
    musicTrained = False

    print('Welcome to the {} music generator!'.format(TEAM))
    while True:
        userInput = mainMenu.getChoice()

        if userInput == 1:
            if not lyricsTrained:
                print('Starting lyrics generator...')
                lyricsModel = trainLyricModels(LYRICSDIRS)
                lyricsTrained = True

            runLyricsGenerator(lyricsModel)

        elif userInput == 2:
            if not musicTrained:
                print('Starting music generator...')
                musicModel = trainMusicModels(MUSICDIRS)
                musicTrained = True

            songName = input('What would you like to name your song? ')
            
            runMusicGenerator(musicModel, WAVDIR + songName + '.wav')

        elif userInput == 3:
            print('Thank you for using the {} music generator!'.format(TEAM))
            sys.exit()

# This is how python tells if the file is being run as main
if __name__ == '__main__':
    main()
    # note that if you want to individually test functions from this file,
    # you can comment out main() and call those functions here. Just make
    # sure to call main() in your final submission of the project!
